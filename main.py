from pytube import YouTube

def progress_func(stream, chunk, bytes_remaining):
    percent_complete = ((stream.filesize - bytes_remaining) / stream.filesize) * 100
    print(f"Download progress: {percent_complete:.2f}%")

def complete_func(): 
    print("Download Complete")
    print("Converting to mp3...")

def format_time(seconds: int) -> str:
    if(seconds > 3600):
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    elif(seconds > 60):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes}:{seconds:02d}"
    else:
        return f"0:{seconds}"

def format_views(views: int) -> str:
    if(views > 1000000):
        return f"{views // 1000000}M"
    elif(views > 1000):
        return f"{views // 1000}K"
    else:
        return f"{views}"      

if __name__ == "__main__":
    yt = YouTube(
            'https://www.youtube.com/watch?v=gZHyG13ZiNM',
            on_progress_callback=progress_func,
            use_oauth=False,
            allow_oauth_cache=True
        )

    print(f"{yt.title} | {format_time(yt.length)} | {format_views(yt.views)} views")

    for item in yt.streams.filter(only_audio = True):
        print(f"{item.itag} | {item.mime_type} | {item.abr} | {item.type}")

    itag = input("Enter item tag of wanted audio: ")
    download_file = yt.streams.get_by_itag(itag)
    download_file.download(filename=f"{yt.title}.{download_file.subtype}")

main()