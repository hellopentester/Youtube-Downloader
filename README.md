# Youtube-Downloader
This repository provides a script to download all videos from a YouTube playlist in 720p MP4 format using yt-dlp.

Prerequisites

Before running the script, make sure you have the following installed:

Python (https://www.python.org/downloads/)

yt-dlp (pip install yt-dlp)

ffmpeg

Installing ffmpeg

To ensure yt-dlp can properly merge video and audio, install ffmpeg by following these steps:

Download ffmpeg from the official site:
🔗 https://ffmpeg.org/download.html

Extract ffmpeg folder (e.g., C:\ffmpeg)

Add ffmpeg/bin to system PATH:

Open Control Panel > System > Advanced system settings

Click Environment Variables

Edit the Path variable in System Variables

Add C:\ffmpeg\bin

Click OK and restart your terminal

Verify ffmpeg installation by running:

ffmpeg -version

Usage

Clone this repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

Install dependencies:

pip install -r requirements.txt

Run the script:

python download_playlist.py

Enter the YouTube playlist URL when prompted.

Notes

Private videos cannot be downloaded unless authenticated.

Ensure ffmpeg is installed to merge video and audio properly.

Happy downloading! 🎥
