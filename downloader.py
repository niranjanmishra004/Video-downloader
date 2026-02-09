import yt_dlp
import os

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'restrictfilenames': True,
        'quiet': False,
        'progress_hooks': [hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except yt_dlp.utils.DownloadError as e:
        print(f"❌ Download failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def hook(d):
    if d['status'] == 'finished':
        print(f"\n🎥 Downloaded: {d.get('filename', 'Unknown')}")

if __name__ == "__main__":
    link = input("Enter video URL (YouTube/Facebook/Instagram): ").strip()
    
    if not link:
        print("❌ No URL provided!")
    elif not link.startswith(('http://', 'https://')):
        print("❌ Invalid URL format!")
    else:
        print("⏳ Downloading...")
        success = download_video(link)
        if success:
            print("✅ Download complete!")
        else:
            print("❌ Download failed!")
