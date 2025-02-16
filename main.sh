# #!/bin/bash
# ###
#  # @Author: Diana Tang
#  # @Date: 2025-02-16 10:32:20
#  # @LastEditors: Diana Tang
#  # @Description: some description
#  # @FilePath: /extract-subtitle/main.sh
# ### 

# # 输入视频文件夹和输出图片文件夹
# input_folder="/path/to/videos"  # 视频文件夹路径
# output_folder="/Users/callustang/tangCode/extract-subtitle/01"  # 输出文件夹路径

# # 确保输出文件夹存在
# mkdir -p "$output_folder"

# # 遍历所有视频文件
# for video in "$input_folder"/*.mp4; do  # 假设所有视频文件都是 .mp4 格式，按需调整
#     # 获取视频文件名（不含路径）
#     video_name=$(basename "$video" .mp4)
    
#     # 提取每秒1帧图像，并保存到输出文件夹
#     ffmpeg -i "$video" -vf "fps=1/2" "$output_folder/${video_name}_frame_%04d.png"
    
#     echo "Processed $video_name"
# done

# echo "Batch video extraction complete!"
#!/bin/bash

# 输入视频文件夹路径
input_folder="./videos"  # 替换为你的文件夹路径

# 遍历视频文件夹中的所有 .mp4 文件
for video in "$input_folder"/*.mp4; do
    # 获取视频文件名（不带扩展名）
    filename=$(basename "$video" .mp4)

    # 创建视频对应的文件夹（如果不存在）
    output_folder="$input_folder/$filename"
    mkdir -p "$output_folder"

    # 使用 FFmpeg 提取每2秒一帧并保存到对应的文件夹
    ffmpeg -i "$video" -vf "fps=1/2" "$output_folder/frame_%04d.png"

    echo "Extracted frames from $video and saved to $output_folder"
done

echo "Batch extraction complete!"

