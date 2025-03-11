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
   git clone https://github.com/hellopentester/Youtube-Downloader.git
   cd Youtube-Downloader![downloading](https://github.com/user-attachments/assets/0a7bdd89-0e8b-4cc4-a2a2-770f0b3bc464)

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

### File Storage

- All downloaded videos will be stored inside the `youtube_downloads` folder.
- A subfolder with the **title of the playlist** will be automatically created to keep files organized.
- Each video file will be saved in `MP4` format using the video title as the filename.

Example folder structure after downloading:
```
youtube_downloads/
 ├── Playlist_Title/
 │   ├── Video1.mp4
 │   ├── Video2.mp4
 │   ├── Video3.mp4
```

## Notes

- Private videos cannot be downloaded unless authenticated.
- Ensure `ffmpeg` is installed to merge video and audio properly.

## Proof of Concept (POC)

Below is an example image showing a successful download process and the resulting file structure:
### Enter prompt
![enter-prompt](https://github.com/user-attachments/assets/9d3618d5-5cd9-49a3-9e48-a5e97d0229c3)

### Downloading
![downloading](https://github.com/user-attachments/assets/e9d9f11c-1935-4b22-88a9-e1e57022121c)

### Completed Download
![completed](https://github.com/user-attachments/assets/2b2b6e7e-81bd-4b2d-b49a-e3b1d13cf5de)



---

### Happy Downloading! 🎥

