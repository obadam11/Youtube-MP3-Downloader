import youtube_dl
import os

url = input("Enter the song's URL: ")
params ={
    'format': 'bestaudio/best',
    'postprocessors':[{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
}

youtube= youtube_dl.YoutubeDL(params)
youtube.download([url])
print("Download Done!")
print("Transfering Files...")

os.system('mv ./*.mp3 /home/*/Music')
