from PIL import Image
import os

# 创建目标目录（如果不存在）
output_folder = "GIFs"
os.makedirs(output_folder, exist_ok=True)

# 遍历每个 PNG 文件并将其转换为 GIF
png_files = [f for f in os.listdir() if f.endswith(".png")]

for png_file in png_files:
    # 打开PNG文件
    image = Image.open(png_file)
    
    # 创建一个新的GIF图像对象
    gif = Image.new("RGBA", image.size)
    
    # 将PNG文件的每一帧添加到GIF图像对象中
    gif.paste(image, (0, 0), image)
    
    # 生成输出文件的路径
    gif_file = os.path.join(output_folder, os.path.splitext(png_file)[0] + ".gif")
    
    # 保存GIF图像
    gif.save(gif_file)
