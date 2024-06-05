from pytube import YouTube

def download_youtube_video_or_audio(url, downloadType, path):
    
    yt = YouTube(url)
   
    print("Title:", yt.title)

    if(downloadType == 'video'):
        stream = yt.streams.get_highest_resolution()
    
    elif (downloadType == 'audio'):
        stream = yt.streams.filter(only_audio = True).first()
    
    else:
        raise ValueError("downloadType must be either 'video' or 'audio'")


    stream.download(path)
    print("Downloaded", downloadType, ":", yt.title)

url = input("Enter the YouTube URL: ")
downloadType = input("Enter 'video' to download video or 'audio' to download audio: ").strip().lower()
path = "Enter_the_path_where_you_want_to_save_video_or_audio"

download_youtube_video_or_audio(url, downloadType, path)