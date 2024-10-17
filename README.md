
# Audio Video Downloader (AVDL)
AVDL is used to download the video and audio files from social media, and convert them to mp4 & mp3 files using yt-dlp.

## Prerequisites
 - Python 3.9 or higher
## Installation

1. Clone this repository or download the main.py script.

2. Install the required Python libraries:

```bash
  pip install yt-dlp
```

## Usage

Run the script from the command line with the following arguments:

```
python main.py --url VIDEO_URL --hardware HARDWARE_TYPE --output_dir OUTPUT_DIRECTORY
```

Replace the following:
- `VIDEO_URL`: Your Video URL
- `HARDWARE_TYPE`: Your Hardware type for Video encoding (choose one [nvidia, amd, cpu])
- `OUTPUT_DIRECTORY`: The directory where you want to save the downloaded files

Example:

```
python main.py --url https://www.youtube.com/watch?v=dQw4w9WgXcQ --hardware nvidia --output_dir ~/Desktop/Down   
```
- `--audio_only`: Add this tag for downloading audio only

## Note

This tool is for personal use only. Respect copyright laws and the terms of service of YouTube. Make sure you have the right to download and use the content.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.