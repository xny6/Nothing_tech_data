import os

# 设置源文件夹和输出文件路径
input_folder = 'S:\AI REU\Support_center/txt_output'  # ← 替换成你的文件夹路径
output_file = 'merged_output_final.txt'   # 输出的合并文件名，可改为绝对路径

# 创建一个空字符串用于保存所有文本
all_text = ""

# 遍历文件夹中的所有 .txt 文件
for filename in sorted(os.listdir(input_folder)):
    if filename.endswith('.txt'):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            all_text += content + '\n\n\n\n\n\n\n\n\n\n\n\n\n'  # 每个文件之间用两个换行分隔

# 写入到最终的输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(all_text)

print(f"合并完成，共写入文件：{output_file}")
