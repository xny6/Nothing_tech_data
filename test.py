import os
import pandas as pd

# 输入文件夹（当前目录）
input_folder = '.'

# 输出文件夹
output_folder = 'txt_output'
os.makedirs(output_folder, exist_ok=True)

# 遍历所有 CSV 文件
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(input_folder, filename)
        
        try:
            # 读取 CSV，不使用列名，读取前两列
            df = pd.read_csv(file_path, header=0, usecols=[0, 1], dtype=str, encoding='utf-8', on_bad_lines='skip')

            # 输出文件路径
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_path = os.path.join(output_folder, txt_filename)

            # 写入 txt 文件，每对 Q&A 之间用 TAB 分隔，并增加额外换行
            with open(txt_path, 'w', encoding='utf-8') as f:
                for _, row in df.iterrows():
                    question = str(row.iloc[0]).strip()
                    answer = str(row.iloc[1]).strip()
                    f.write(f"{question}\t{answer}\n\n\n\n\n\n\n")  # 增加一个额外的换行（两个换行总共）

            print(f"转换完成：{filename} -> {txt_filename}")

        except Exception as e:
            print(f"处理文件 {filename} 时出错：{e}")
