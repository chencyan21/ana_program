```python
text = "Hello, world! This is a tokenizer example."
tokens = text.split()  # 简单的分词方法，按空格分割
print(tokens)
# 输出: ['Hello,', 'world!', 'This', 'is', 'a', 'tokenizer', 'example.']

```

    ['Hello,', 'world!', 'This', 'is', 'a', 'tokenizer', 'example.']
    


```python
vocab = {'Hello,': 1, 'world!': 2, 'This': 3, 'is': 4, 'a': 5, 'tokenizer': 6, 'example.': 7}
numericalized_tokens = [vocab[token] for token in tokens]
print(numericalized_tokens)
# 输出: [1, 2, 3, 4, 5, 6, 7]

```

    [1, 2, 3, 4, 5, 6, 7]
    


```python
import torch.nn as nn
import torch
# 假设词汇表大小为 8，嵌入维度为 3
embedding = nn.Embedding(10, 3)

# 将数值化后的 token 转换为嵌入向量
embedded_tokens = embedding(torch.tensor(numericalized_tokens))
print(embedded_tokens)
# 输出: tensor形状为 (7, 3) 的嵌入向量

```

    tensor([[-0.1641, -1.1500, -0.3002],
            [ 1.2479,  0.4111, -0.2258],
            [-0.8492, -0.5455, -0.3239],
            [ 0.8626,  0.1890,  1.2637],
            [-0.9000,  1.3115,  1.0512],
            [-1.5201, -0.3557,  1.2839],
            [ 0.6551,  0.4738, -0.7963]], grad_fn=<EmbeddingBackward0>)
    


```python
import torch
print(torch.cuda.is_available())
```

    False
    
