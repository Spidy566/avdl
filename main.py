import argparse
import yt_dlp
import os

def video_encoding(hardware: str):
    encoding_options = {
        'nvidia': ['-c:v', 'h264_nvenc'],
        'amd': ['-c:v', 'h264_amf'],
        'cpu': ['-c:v', 'libx264']
    }
    
    if hardware not in encoding_options:
        raise ValueError('Invalid hardware option')

    return encoding_options[hardware] + ['-c:a', 'aac', '-b:a', '192k']

def downloader(url: str, output_dir: str, hardware: str, audio_only: bool):
    base_ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'default_search': 'ytsearch',
        'quiet': True,
        'no_warnings': True
    }

    if audio_only:
        ydl_opts = {
            **base_ydl_opts,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        }
    else:
        ydl_opts = {
            **base_ydl_opts,
            'format': 'bestvideo*+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'postprocessor_args': video_encoding(hardware)
        }

    while True:
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print('Download completed')
            break
        except yt_dlp.DownloadError as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download and convert YouTube video')
    parser.add_argument('--url', type=str, help='URL of the video', required=True)
    parser.add_argument('--output_dir', type=str, help='Output directory', required=True)
    parser.add_argument('--hardware', type=str, help='Use hardware acceleration for video encoding (nvidia, amd, cpu)',choices=['nvidia', 'amd', 'cpu'])
    parser.add_argument('--audio_only', action='store_true', help='Download audio only')

    args = parser.parse_args()


    downloader(args.url, args.output_dir, args.hardware, args.audio_only)


