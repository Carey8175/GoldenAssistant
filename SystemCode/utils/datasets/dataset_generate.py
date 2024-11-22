from SystemCode.utils.datasets.video2picture import extract_frames


def generate_raw_dataset(video_path, output_folder, video_id, frame_per_second=2):
    """
    生成原始数据集，从视频数据中提取帧图像
    :param video_path:
    :param output_folder:
    :param video_id:
    :param frame_per_second: 压缩比率
    :return:
    """
    # 提取视频帧
    extract_frames(video_path, output_folder, video_id, frame_per_second)


if __name__ == '__main__':
    # 设置视频文件路径
    video_path = "1.mp4"

    # 设置输出文件夹路径
    output_folder = "../../statics/detection_data/raw"

    # 提取视频帧
    generate_raw_dataset(video_path, output_folder, video_id=1, frame_per_second=100)
