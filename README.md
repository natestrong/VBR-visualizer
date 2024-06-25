# VBR Visualizer
## Overview
The purpose of this project is to analyze the variable bit rate (VBR) encoding of different video codecs by examining the frame sizes throughout a video sequence. The project generates charts to visually represent the frame sizes and compare them against the target and maximum bitrates defined by the codecs.

The project takes a HDR Rec. 2020 video file as input and generates a series of charts for each codec. The charts show the frame sizes in kilobytes (KB) for each frame in the video sequence. The target and maximum bitrates are also displayed on the charts for comparison.
![Movie Legend](output/movie_legend.png)

The target bitrates for different codecs are defined in codec_target_bitrates.py. The bitrate provided is from developer documentation and is accurate for 29.97 fps. However, my project uses 24fps video, so I convert the target bitrates at runtime for 24fps.
```python
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
}
```

# Findings

Below are the charts generated from analyzing the test footage. Each chart shows the frame sizes in KB, along with the target and maximum frame sizes for comparison.

	•	ProRes 4444 XQ
![ProRes 4444 XQ](output/ProRes_4444_XQ.png)

    •	ProRes 4444
![ProRes 4444](output/ProRes_4444.png)

    •	ProRes 422 HQ
![ProRes 422 HQ](output/ProRes_422_HQ.png)

    •	ProRes 422
![ProRes 422](output/ProRes_422.png)

    •	ProRes 422 LT
![ProRes 422 LT](output/ProRes_422_LT.png)

    •	ProRes 422 Proxy
![ProRes 422 Proxy](output/ProRes_422_Proxy.png)
