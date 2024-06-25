# codec_target_bitrates.py

CODEC_TARGET_BITRATES = {
    'ProRes 4444 XQ': {'bitrate': 500, 'filename': 'prores4444xq'},
    'ProRes 4444': {'bitrate': 330, 'filename': 'prores4444'},
    'ProRes 422 HQ': {'bitrate': 220, 'filename': 'prores422hq'},
    'ProRes 422': {'bitrate': 147, 'filename': 'prores422'},
    'ProRes 422 LT': {'bitrate': 102, 'filename': 'prores422lt'},
    'ProRes 422 Proxy': {'bitrate': 45, 'filename': 'prores422proxy'},
    'DNxHR HQX': {'bitrate': 666, 'filename': 'dnxhr_hqx'},
    'DNxHR HQ': {'bitrate': 666, 'filename': 'dnxhr_hq'},
    'DNxHR SQ': {'bitrate': 441, 'filename': 'dnxhr_sq'},
    'DNxHR LB': {'bitrate': 137, 'filename': 'dnxhr_lb'},
    'H264': {'bitrate': 16, 'filename': 'h264'},
}

# Adjust bitrates for 24fps
FPS_ADJUSTMENT_RATIO = 24 / 29.97
for codec in CODEC_TARGET_BITRATES:
    CODEC_TARGET_BITRATES[codec]['bitrate'] *= FPS_ADJUSTMENT_RATIO
