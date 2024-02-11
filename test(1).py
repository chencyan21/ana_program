from tqdm.notebook import tqdm
from rich.progress import Progress

# 创建一个进度条对象
progress = Progress()

# 获取或创建一个任务对象
task = progress.add_task("[cyan]Processing...", total=10)

# 在循环中更新进度条
for i in range(10):
    # 在任务中更新进度条
    progress.update(task, advance=1)
    # 执行你的循环体内的代码
# 完成后清理并显示进度条
progress.stop()
