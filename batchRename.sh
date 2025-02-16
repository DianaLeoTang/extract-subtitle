#!/bin/bash
###
 # @Author: Diana Tang
 # @Date: 2025-02-16 10:36:21
 # @LastEditors: Diana Tang
 # @Description: some description
 # @FilePath: /extract-subtitle/rename.sh
### 

# 输入文件夹路径
input_folder="./videos"  # 替换为你的文件夹路径

# 遍历文件夹中的所有 .mp4 文件
for file in "$input_folder"/*.mp4; do
    # 获取文件名（去掉路径）
    filename=$(basename "$file")

    # 使用正则表达式删除文件名中的 "01-" 或 "02-" 后面的内容
    if [[ "$filename" =~ ^(01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17)- ]]; then
        new_filename="${filename%%-*}.mp4"  # 删除从 "-" 后面的所有内容
        mv "$file" "$input_folder/$new_filename"  # 重命名文件
        echo "Renamed $filename to $new_filename"
    fi
done

echo "Batch rename complete!"
