import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    link = input("Enter video URL (YouTube/Facebook/Instagram): ")
    download_video(link)
    print("✅ Download complete!")
