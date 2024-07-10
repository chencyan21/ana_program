# text-preprocessing
import torch, random, re, collections


# 词元化
def tokenize(strings, token="word"):
    if token == "word":
        return [str.split() for str in strings]
    elif token == "char":
        return [list(str) for str in strings]
    else:
        print("Wrong!")


# 统计词元的频率
def count_corpus(tokens):
    if len(tokens) == 0 or isinstance(tokens[0], list):
        tokens = [token for line in tokens for token in line]
    return collections.Counter(tokens)


# 加载语料库和词典
def load_cropus(max_tokens=-1, file_name="timemachine", pattern="char"):
    with open(f"./MLModel/data/{file_name}.txt", "r") as f:
        lines = f.readlines()
    lines = [re.sub("[^A-Za-z]+", " ", line).strip().lower() for line in lines]
    tokens = tokenize(lines, pattern)
    vocab = Vocabulary(tokens=tokens, min_freq=0)
    corpus = [vocab[token] for line in tokens for token in line]
    if max_tokens > 0:
        corpus = corpus[:max_tokens]
    return corpus, vocab


# 随机采样
def seq_data_iter_random(corpus, batch_size, num_steps, random_offset="True"):
    if random_offset:
        a = random.randint(0, num_steps - 1)
        # 如果偏移量大于时间步x，则偏移量中的x可以作为新的时间步
    else:
        a = 0
    print(f"random offset: {a}")
    # update corpus
    corpus = corpus[a:]
    num_subseqs = (len(corpus) - 1) // num_steps
    initial_indices = [i * num_steps for i in range(num_subseqs)]
    random.shuffle(initial_indices)
    num_batches = num_subseqs // batch_size
    for i in range(0, num_batches * batch_size, batch_size):
        initial_indices_per_batch = initial_indices[i : i + batch_size]
        X = [corpus[j : j + num_steps] for j in initial_indices_per_batch]
        Y = [corpus[j + 1 : j + num_steps + 1] for j in initial_indices_per_batch]
        yield torch.tensor(X), torch.tensor(Y)


# 顺序分区
def seq_data_iter_sequential(corpus, batch_size, num_steps):  # @save
    offset = random.randint(0, num_steps - 1)
    offset = 0
    corpus = corpus[offset:]
    num_tokens = ((len(corpus) - 1) // batch_size) * batch_size
    Xs = torch.tensor(corpus[0:num_tokens]).reshape(batch_size, -1)
    Ys = torch.tensor(corpus[1 : num_tokens + 1]).reshape(batch_size, -1)
    num_batches = num_tokens // (batch_size * num_steps)
    for i in range(0, num_batches):
        X = Xs[:, i * num_steps : (i + 1) * num_steps]
        Y = Ys[:, i * num_steps : (i + 1) * num_steps]
        yield X, Y


def load_data_time_machine(
    batch_size, num_steps, use_random_iter=False, max_tokens=10000
):
    data_iter = SeqDataLoader(
        batch_size, num_steps, use_random_iter=use_random_iter, max_tokens=max_tokens
    )
    return data_iter, data_iter.vocab


# 词表
class Vocabulary:
    def __init__(self, tokens=None, min_freq=0, reversed_tokens=None) -> None:
        if tokens == None:
            tokens = []
        if reversed_tokens == None:
            reversed_tokens = []
        counter = count_corpus(tokens)
        self._token_freqs = sorted(counter.items(), key=self.cmp, reverse=True)
        self.idx_to_token = ["<unk>"] + reversed_tokens
        self.token_to_idx = {token: idx for idx, token in enumerate(self.idx_to_token)}
        for token, freq in self._token_freqs:
            if freq < min_freq:
                break  # 后面的不加入到词表中
            if token not in self.token_to_idx:
                self.token_to_idx[token] = len(self.idx_to_token)
                self.idx_to_token.append(token)

    def cmp(self, x):
        return x[1]

    @property
    def unk(self):
        return 0

    @property
    def token_freqs(self):
        return self._token_freqs

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.to_tokens(indice) for indice in indices]


class SeqDataLoader:
    def __init__(self, batch_size, num_steps, use_random_iter, max_tokens) -> None:
        if use_random_iter:
            self.data_iter_fn = seq_data_iter_random
        else:
            self.data_iter_fn = seq_data_iter_sequential
        self.corpus, self.vocab = load_cropus(max_tokens, pattern="word")
        self.batch_size, self.num_steps = batch_size, num_steps

    def __iter__(self):
        return self.data_iter_fn(self.corpus, self.batch_size, self.num_steps)


# 读取数据集
with open("./MLModel/data/timemachine.txt", "r") as f:
    lines = f.readlines()
lines = [re.sub("[^A-Za-z]+", " ", line).strip().lower() for line in lines]

tokens = tokenize(lines, token="word")
vocab = Vocabulary(tokens)
print(list(vocab.token_to_idx.items())[:10])
print(vocab["ads"])
for i in [0, 10]:
    print("文本:", tokens[i])
    print("索引:", vocab[tokens[i]])
corpus, vocab = load_cropus(pattern="word")
len(corpus), len(vocab)
