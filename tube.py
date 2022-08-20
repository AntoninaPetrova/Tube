from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=cot8q5pftm8")
yt = yt.get('mp4', '720p')
yt.download('C:\\Users\\user\\Videos')