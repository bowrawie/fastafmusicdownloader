from __future__ import unicode_literals
import youtube_dl
import os
import sys
from pyperclip import paste as pasta
from pathlib import Path

def DOWNLOADER(SL):
    fileName = Path("Songs")
     
    if (os.path.isdir(fileName)):
        print("ok")     
    else :
        os.mkdir("Songs")
        
        
    download_options = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'nocheckcertificate': True,
            'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
            }],
    }
    try:
            
            with youtube_dl.YoutubeDL(download_options) as dl:
                    dl.download([SL])
            for fileName in os.listdir():
                    if(".mp3" in fileName):
                            os.rename(fileName,"Songs\\"+fileName)                              
    except NameError as e :
            input(e)
			


