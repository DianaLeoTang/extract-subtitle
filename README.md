<!--
 * @Author: Diana Tang
 * @Date: 2025-02-14 20:47:50
 * @LastEditors: Diana Tang
 * @Description: some description
 * @FilePath: /extract-subtitle/README.md
-->
# extract-subtitle
提取视频中的字幕文件，进行视频总结和学习


# 安装 ffmpeg
sudo apt-get install ffmpeg    # Ubuntu
brew install ffmpeg            # macOS

# 安装 pytesseract 和 Pillow（用于图像处理）
pip install pytesseract pillow

pip install tesseract-ocr-chi-sim  # 安装简体中文语言包

sudo apt-get install tesseract-ocr-chi-tra  # 安装繁体中文语言包

brew install tesseract-lang

ffmpeg -i /Users/aaa/extract-subtitle/videos/01.mp4 -vf "fps=1" /Users/aaa/extract-subtitle/01/output_frame_%04d.png


在终端中，进入脚本文件所在的目录，并运行以下命令为脚本添加可执行权限：
chmod +x main.sh

执行脚本来批量处理视频：
./main.sh
