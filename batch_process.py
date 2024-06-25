import os
import subprocess
from codec_target_bitrates import CODEC_TARGET_BITRATES

# Path to the folder containing the files to process
input_folder = os.path.join(os.path.dirname(__file__), 'test_footage/h264_rec709')
output_folder = os.path.join(os.path.dirname(__file__), 'output')


# Function to find the format label and target bitrate from the file name
def get_format_label_and_target(file_name):
    file_name_lower = file_name.lower()
    for format_label, codec_info in CODEC_TARGET_BITRATES.items():
        if file_name_lower.endswith(codec_info['filename'] + '.mov'):
            target_bitrate = codec_info['bitrate']
            return format_label, target_bitrate
    return None, None


# Iterate over each file in the input folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)
    # if "422HQ" not in file_name:
    #     continue
    if os.path.isfile(file_path):
        format_label, target_bitrate = get_format_label_and_target(file_name)
        if format_label and target_bitrate:
            print(f'Processing {file_name} with label {format_label} and target bitrate {target_bitrate:.2f} MB/s')
            subprocess.run([
                'python', 'app.py',
                '--movie', file_path,
                '--output', output_folder,
                '--format_label', format_label,
                '--target_bitrate', str(target_bitrate)
            ])
        else:
            print(f'Skipping {file_name}, no matching format label found.')

print('Batch processing complete.')
