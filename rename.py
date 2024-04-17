import os
import re

def rename_files_in_folder(folder_path):
    # 获取文件夹中所有文件列表
    files = os.listdir(folder_path)
    # 用正则表达式匹配文件名中的数字
    pattern = re.compile(r'\d+')

    for filename in files:
        if filename.lower().endswith('.wav'):
            # 获取文件的完整路径
            old_file = os.path.join(folder_path, filename)
            # 查找文件名中的数字
            match = pattern.search(filename)
            if match:
                new_filename = f"{match.group()}.wav"
                new_file = os.path.join(folder_path, new_filename)
                # 重命名文件
                os.rename(old_file, new_file)
                print(f"Renamed '{filename}' to '{new_filename}'")

# 使用示例，记得将folder_path更改为你的文件夹路径
folder_path = 'dataset_diverse_sample/demo_s3_02_diverse_v4'
rename_files_in_folder(folder_path)


# # 使用示例，记得将folder_path更改为你的文件夹路径
# folder_path = 'dataset_diverse_sample/demo_s3_02_diverse_v2'
# rename_files_in_folder(folder_path, start_number=1)
