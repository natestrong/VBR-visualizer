import argparse
import os
import ffmpeg
import matplotlib.pyplot as plt
import numpy as np


def extract_frame_sizes(video_path):
    # Run ffprobe command to get frame information
    try:
        result = ffmpeg.probe(video_path, select_streams='v', show_entries='frame=pkt_size', of='json')
        frames_info = result
        frame_sizes = [int(frame['pkt_size']) / 1024 for frame in frames_info['frames']]  # Convert bytes to KB
        return frame_sizes
    except ffmpeg.Error as e:
        print(f"An error occurred while running ffprobe: {e.stderr}")
        return []


def plot_frame_sizes(frame_sizes, output_path, format_label, target_bitrate=None, file_size=None):
    frames = np.arange(len(frame_sizes))

    plt.figure(figsize=(10, 6))  # Increase figure height slightly
    plt.plot(frames, frame_sizes, label='Frame Size (KB)')

    if target_bitrate:
        # Calculate the target size per frame
        target_size_per_frame = (
                                        target_bitrate * 1000 * 1000) / 8 / 24  # Convert mbps to bytes per second, then to bytes per frame at 24fps
        target_size_per_frame /= 1024  # Convert bytes to KB
        plt.axhline(y=target_size_per_frame, color='g', linestyle='--', label='Target')
        plt.text(len(frames) - 1, target_size_per_frame, f'{int(target_size_per_frame)} KB', color='g', va='center',
                 ha='left', backgroundcolor='w')

    max_size = np.max(frame_sizes)
    plt.axhline(y=max_size, color='r', linestyle='--', label='Max')
    plt.text(len(frames) - 1, max_size, f'{int(max_size)} KB', color='r', va='center', ha='left', backgroundcolor='w')

    plt.xlabel('Frame')
    plt.ylabel('Frame Size (KB)')
    plt.title(f'{format_label} (Target: {int(target_bitrate)} MB/s)' if target_bitrate else f'{format_label}')

    # Adjust layout to make space for file size at the bottom
    plt.subplots_adjust(bottom=0.15)

    # Add file size at the bottom
    if file_size:
        plt.figtext(0.5, 0.01, f'File Size: {file_size} MB', ha='center', fontsize=10)

    plt.legend()  # Bring back the legend

    # Save the plot
    file_path = os.path.join(output_path, f'{format_label}.png')
    version = 1
    while os.path.exists(file_path):
        file_path = os.path.join(output_path, f'{format_label}_v{version}.png')
        version += 1

    plt.savefig(file_path)
    plt.close()


def get_file_size(video_path):
    return os.path.getsize(video_path) / (1024 * 1024)  # Convert bytes to MB


def main(movie_path, output_path, format_label, target_bitrate):
    if not os.path.exists(movie_path):
        print(f"Error: The movie file '{movie_path}' does not exist.")
        return

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    frame_sizes = extract_frame_sizes(movie_path)
    file_size = get_file_size(movie_path)

    if frame_sizes:
        plot_frame_sizes(frame_sizes, output_path, format_label, target_bitrate, int(file_size))
        print(f"Chart has been created and saved to {output_path}")
    else:
        print("Failed to extract frame sizes.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Analyze video file frame sizes and create a chart.')
    parser.add_argument('--movie', help='Path to the movie file.')
    parser.add_argument('--output', help='Folder location to output the chart.')
    parser.add_argument('--format_label', help='Label for the format to be used as the chart title.')
    parser.add_argument('--target_bitrate', type=float, help='Target bitrate for the codec.')

    args = parser.parse_args()

    # Default test logic
    movie_path = args.movie or 'test_footage/ProRes_rec2020/vbr-tester-01_v01_rec2020_ProRes4444XQ.mov'
    output_path = args.output or 'output'
    format_label = args.format_label or 'ProRes 4444 QX'
    target_bitrate = args.target_bitrate or 400

    main(movie_path, output_path, format_label, target_bitrate)
