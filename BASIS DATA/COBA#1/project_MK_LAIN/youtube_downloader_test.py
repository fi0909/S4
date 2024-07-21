from pytube import YouTube
from PIL import Image
import urllib.request
from io import BytesIO
def prog_bar(stream,chunk,bytes_remaining):
    progress = int(((stream.filesize-bytes_remaining)/stream.filesize)*100)
    print(progress)

link = 'https://www.youtube.com/watch?v=gBt9kSpQCBk'
yt =YouTube(link,on_progress_callback=prog_bar)
u = urllib.request.urlopen(yt.thumbnail_url)
raw_data = u.read()
u.close()
im = Image.open(BytesIO(raw_data))
strm = yt.streams.filter(only_audio=True)
yd = yt.streams.get_audio_only()
im.show()
print(strm)
print(yd)
print()