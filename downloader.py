from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv

# Download data and Config

download_options = {
    'format' : 'bestaudio/best', #Select the best quality audio only-format. 
    'outtmpl' : '%(title)s.%(ext)s',
    'nocheckcertificate' : True,
    'postprocessors' : [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192',
    }],
}

#Song directory
if not os.path.exists('Songs'):
    os.mkdir('Songs')
else:
    os.chdir('Songs')

#Download Songs
with youtube_dl.YoutubeDL(download_options) as dl:
    with open('../' + argv[1], 'r') as f:
        for song_url in f:
            dl.download([song_url])