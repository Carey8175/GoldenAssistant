import cv2
import os
from concurrent.futures import ThreadPoolExecutor


def save_frame(frame, frame_filename):
    # 保存单个帧
    cv2.imwrite(frame_filename, frame)
    print(f"Saved {frame_filename}")


def extract_frames(video_path, output_folder, video_order, interval=2):
    # 确保输出文件夹存在
    os.makedirs(output_folder, exist_ok=True)

    # 打开视频文件
    video_capture = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not video_capture.isOpened():
        print("Error: Failed to open video file.")
        return

    frame_count = 0
    saved_frame_count = 0

    # 使用线程池来保存帧图像
    with ThreadPoolExecutor() as executor:
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            # 生成图像文件名
            frame_filename = f"{output_folder}/{video_order}_frame_{frame_count:04d}.jpg"

            # 仅按间隔保存指定帧
            if frame_count % interval == 0:
                executor.submit(save_frame, frame, frame_filename)
                saved_frame_count += 1

            print(f"Extracting frame {frame_count}")
            frame_count += 1

    # 关闭视频文件
    video_capture.release()
    print(f"Frames extracted: {frame_count}, Frames saved: {saved_frame_count}")
