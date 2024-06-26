import os
import subprocess


def extract_prores_frame(video_path, output_frame_path, frame_number):
    command = [
        'ffmpeg', '-i', video_path, '-vf', f'select=eq(n\\,{frame_number})', '-vsync', 'vfr',
        '-update', '1', '-frames:v', '1', output_frame_path, '-y'
    ]
    subprocess.run(command, check=True)


def generate_difference_image(prores_frame, exr_frame, output_diff_image):
    command = [
        'ffmpeg', '-i', prores_frame, '-i', exr_frame, '-filter_complex', 'blend=all_mode=difference',
        output_diff_image, '-y'
    ]
    subprocess.run(command, check=True)


def compute_psnr(prores_frame, exr_frame):
    command = [
        'ffmpeg', '-i', prores_frame, '-i', exr_frame, '-lavfi', 'psnr', '-f', 'null', '-'
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    psnr_output = result.stderr
    psnr_value = psnr_output.split('average:')[1].split()[0]
    return psnr_value


def compute_ssim(prores_frame, exr_frame):
    command = [
        'ffmpeg', '-i', prores_frame, '-i', exr_frame, '-lavfi', 'ssim', '-f', 'null', '-'
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    ssim_output = result.stderr
    ssim_value = ssim_output.split('All:')[1].split()[0]
    return ssim_value


def compare_quality(prores_videos_dir, exr_frames_dir, frame_number, output_dir):
    for video_file in os.listdir(prores_videos_dir):
        if video_file.endswith('.mov'):
            video_path = os.path.join(prores_videos_dir, video_file)
            prores_frame_path = os.path.join(output_dir, f'prores_frame_{frame_number}.png')
            diff_image_path = os.path.join(output_dir, f'diff_frame_{frame_number}.png')

            extract_prores_frame(video_path, prores_frame_path, frame_number)

            exr_frame_path = os.path.join(exr_frames_dir, f'vbr-tester-01_v01_aces2065.{frame_number:04d}.exr')
            if os.path.exists(exr_frame_path):
                generate_difference_image(prores_frame_path, exr_frame_path, diff_image_path)

                psnr_value = compute_psnr(prores_frame_path, exr_frame_path)
                ssim_value = compute_ssim(prores_frame_path, exr_frame_path)

                print(f'Comparison for {video_file} at frame {frame_number}:')
                print(f'PSNR: {psnr_value}')
                print(f'SSIM: {ssim_value}')
                print(f'Difference image saved at {diff_image_path}')
                print('-' * 50)
            else:
                print(f'EXR frame not found: {exr_frame_path}')


if __name__ == '__main__':
    PRORES_DIR = '/Users/nstrong/IdeaProjects/VBR-visualizer/test_footage/ProRes_aces2065'
    EXR_DIR = '/Users/nstrong/IdeaProjects/VBR-visualizer/test_footage/vbr-tester-01_v01'
    OUTPUT_DIR = '/Users/nstrong/IdeaProjects/VBR-visualizer/output'
    FRAME_NUMBER = 100  # Change to the frame number you want to compare

    compare_quality(PRORES_DIR, EXR_DIR, FRAME_NUMBER, OUTPUT_DIR)
