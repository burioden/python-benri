# ダウンロードしたwebawardまでのパスを記入 例：ダウンロードフォルダの中に「webaward」入れた場合
download_folder = "/Users/zzz/Downloads/webaward"

import os
import subprocess

directories = [name for name in os.listdir(download_folder) if os.path.isdir(os.path.join(download_folder, name))]

directories.sort()

for directory in directories:
    index_html_path = os.path.join(download_folder, directory, "index.html")
    if os.path.isfile(index_html_path):
        subprocess.Popen(["open", index_html_path])  # mac
        # subprocess.Popen(["start", index_html_path], shell=True)  # Windows
    else:
        print(f"index.html が {directory}. の直下にありませんでした")
