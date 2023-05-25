import os
from sys import argv
import shutil

directory = None
image_exts = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg")
app_exts = (".AppImage", ".deb", ".rpm", ".exe", ".bash", ".bat", ".sh", ".bin", ".msi")
zip_exts = (".tar", ".zip", ".zipx", ".gz", ".rar", ".7z")
video_exts = (".mp4", ".mkv", ".webm", ".mpeg", ".mpg", ".wmv")
text_exts = (".doc", ".docx", ".wps", ".ebook", ".pdf", ".txt", ".md", ".epub")
try:
    directory = argv[1]
except:
    print(f"usage: python3 orgnizer.py /home/xle0x/Downloads")
    print()
    print(f"usage: python3 orgnizer.py `pwd`")

if directory != None:
    for file_name in os.listdir(directory):  # test.png
        if (
            not file_name.endswith(image_exts)
            and not file_name.endswith(zip_exts)
            and not file_name.endswith(app_exts)
            and not file_name.endswith(video_exts)
            and not file_name.endswith(text_exts)
        ):
            if not os.path.exists(file_name.split(".")[-1]):
                os.makedirs(file_name.split(".")[-1])
            shutil.move(file_name, file_name.split(".")[-1])
        else:
            if file_name.endswith(image_exts):
                if not os.path.exists("Images"):
                    os.makedirs("Images")
                shutil.move(file_name, "Images")

            if file_name.endswith(app_exts):
                if not os.path.exists("Apps"):
                    os.makedirs("Apps")
                shutil.move(file_name, "Apps")

            if file_name.endswith(zip_exts):
                if not os.path.exists("Zips"):
                    os.makedirs("Zips")
                shutil.move(file_name, "Zips")

            if file_name.endswith(video_exts):
                if not os.path.exists("Videos"):
                    os.makedirs("Videos")
                shutil.move(file_name, "Videos")

            if file_name.endswith(text_exts):
                if not os.path.exists("Text"):
                    os.makedirs("Text")
                shutil.move(file_name, "Text")
