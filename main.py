'''
Author: Diana Tang
Date: 2025-02-14 20:53:14
LastEditors: Diana Tang
Description: some description
FilePath: /extract-subtitle/main.py
'''
# import os
# import subprocess
# import pytesseract
# from PIL import Image
# import cv2

# # 设置tesseract可执行文件路径（如果需要）
#   # 视你的安装路径而定

# def extract_frames_from_video(video_path, frame_rate=1):
#     """从视频中提取帧，默认每秒提取1帧"""
#     video = cv2.VideoCapture(video_path)
#     frame_count = 0
#     frames = []
    
#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break
#         if frame_count % frame_rate == 0:  # 每隔frame_rate秒提取一帧
#             frames.append(frame)
#         frame_count += 1
    
#     video.release()
#     return frames

# def extract_text_from_frame(frame):
#     """从单个视频帧中提取文本"""
#     # 将图像转为灰度图
#     gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     # 使用Tesseract提取文字
#     text = pytesseract.image_to_string(gray_frame)
#     return text

# def extract_text_from_video(video_path, output_text_path, frame_rate=1):
#     """从视频中提取所有文本并保存到文件"""
#     frames = extract_frames_from_video(video_path, frame_rate)
    
#     with open(output_text_path, 'w', encoding='utf-8') as f:
#         for frame in frames:
#             text = extract_text_from_frame(frame)
#             if text.strip():  # 如果识别到的文本不为空
#                 f.write(text + "\n")
#                 print("提取到文本:", text)

# def extract_text_from_folder(folder_path, frame_rate=1):
#     """从文件夹中所有的视频文件提取文本"""
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):  # 支持的文件格式
#             video_path = os.path.join(folder_path, file_name)
#             output_text_path = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.txt")
#             extract_text_from_video(video_path, output_text_path, frame_rate)

# # 使用示例
# folder_path = "./videos"  # 替换成你的视频文件夹路径
# extract_text_from_folder(folder_path, frame_rate=1)  # 每秒提取1帧

import os
import cv2
import pytesseract
from PIL import Image

# 设置 Tesseract 可执行文件路径（如果需要）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # 视你的安装路径而定

def extract_frames_from_video(video_path, frame_rate=1):
    """从视频中提取帧，默认每秒提取1帧"""
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    frames = []
    
    while True:
        ret, frame = video.read()
        if not ret:
            break
        if frame_count % frame_rate == 0:  # 每隔frame_rate秒提取一帧
            frames.append(frame)
        frame_count += 1
    
    video.release()
    return frames

def extract_text_from_frame(frame):
    """从单个视频帧中提取文本"""
    # # 将图像转为灰度图（有时对OCR更有效）
    # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # # 对图像进行二值化处理，增强文本对比度
    # _, binary_frame = cv2.threshold(gray_frame, 150, 255, cv2.THRESH_BINARY)

    # # 使用 Tesseract 提取文字，指定语言为简体中文（chi_sim）
    # text = pytesseract.image_to_string(binary_frame, lang='chi_sim')
    # return text.strip()  # 移除多余的空格和换行
    # 假设字幕区域位于视频画面的下方，我们可以通过指定区域来裁剪字幕区域
    height, width, _ = frame.shape

    # 假设字幕区域大致在画面下方的 10% 高度范围
    subtitle_area = frame[int(height * 0.85):height, 0:width]  # 裁剪画面下方的 15%

    # 将字幕区域转为灰度图
    gray_frame = cv2.cvtColor(subtitle_area, cv2.COLOR_BGR2GRAY)
    
    # 对图像进行二值化处理，增强文本对比度
    _, binary_frame = cv2.threshold(gray_frame, 150, 255, cv2.THRESH_BINARY)

    # 使用 Tesseract 提取文字，指定语言为简体中文（chi_sim）
    text = pytesseract.image_to_string(binary_frame, lang='chi_sim')
    return text.strip()  # 移除多余的空格和换行

def extract_text_from_video(video_path, output_text_path, frame_rate=1):
    """从视频中提取所有文本并保存到文件"""
    frames = extract_frames_from_video(video_path, frame_rate)
    
    with open(output_text_path, 'w', encoding='utf-8') as f:
        for frame in frames:
            text = extract_text_from_frame(frame)
            if text:  # 如果识别到的文本不为空
                f.write(text + "\n")
                print("提取到字幕:", text)

def extract_text_from_folder(folder_path, frame_rate=1):
    """从文件夹中所有的视频文件提取文本"""
    for file_name in os.listdir(folder_path):
        if file_name.endswith(('.mp4', '.mkv', '.avi', '.mov')):  # 支持的文件格式
            video_path = os.path.join(folder_path, file_name)
            output_text_path = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}.txt")
            extract_text_from_video(video_path, output_text_path, frame_rate)

# 使用示例
folder_path = "./videos"  # 替换成你的视频文件夹路径
extract_text_from_folder(folder_path, frame_rate=2)  # 每2秒提取1帧

