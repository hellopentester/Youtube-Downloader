# YouTube Playlist Downloader

This repository provides a script to download all videos from a YouTube playlist in 720p MP4 format using `yt-dlp`.

## Prerequisites

Before running the script, make sure you have the following installed:

- **Python**: [Download here](https://www.python.org/downloads/)
- **yt-dlp**: Install via pip:
  ```sh
  pip install yt-dlp
  ```
- **ffmpeg**

### Installing ffmpeg

To ensure `yt-dlp` can properly merge video and audio, install `ffmpeg` by following these steps:

1. **Download ffmpeg** from the official site:  
   🔗 [FFmpeg Download](https://ffmpeg.org/download.html)
2. **Extract ffmpeg folder** (e.g., `C:\ffmpeg`)
3. **Add `ffmpeg/bin` to system PATH**:
   - Open **Control Panel** → **System** → **Advanced system settings**
   - Click **Environment Variables**
   - Edit the **Path** variable in **System Variables**
   - Add `C:\ffmpeg\bin`
   - Click **OK** and restart your terminal

4. **Verify ffmpeg installation** by running:
   ```sh
   ffmpeg -version
   ```

## Usage

1. **Clone this repository:**
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the script:**
   ```sh
   python download_playlist.py
   ```
4. **Enter the YouTube playlist URL when prompted.**

## Notes

- Private videos cannot be downloaded unless authenticated.
- Ensure `ffmpeg` is installed to merge video and audio properly.

---

### Happy Downloading! 🎥

