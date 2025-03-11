import yt_dlp
import os

# Meminta input URL playlist dari pengguna
playlist_url = input("Masukkan URL Playlist YouTube: ")

# Mengambil informasi playlist untuk mendapatkan judul
with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    playlist_title = info.get('title', 'Playlist_Undefined').replace(" ", "_")

# Membuat folder dengan nama sesuai judul playlist
output_folder = f"youtube_downloads/{playlist_title}"
os.makedirs(output_folder, exist_ok=True)

# Opsi download (video 720p dengan audio terbaik, format MP4)
ydl_opts = {
    'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
    'merge_output_format': 'mp4',
    'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
    'ignoreerrors': True,  # Lewati video yang tidak bisa diunduh (termasuk private)
}

# Download semua video dalam playlist
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print(f"Semua video telah selesai di-download ke folder: {output_folder}")
