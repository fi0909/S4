
from pytube import YouTube
from pytube.cli import on_progress
link="https://www.youtube.com/watch?v=ZIY81FE-mZE"
youtube=YouTube(link,on_progress_callback=on_progress)
strm = youtube.streams.filter(adaptive=True,only_video=True,resolution="1080p").first()
if strm is not None: 
    strm.download('C:/Users/croco/OneDrive/Documents/Project asal/P1/tester')
