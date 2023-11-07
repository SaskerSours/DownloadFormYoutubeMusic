from moviepy.editor import *


# audio_clip = AudioFileClip("C:\\Users\\horob\\NewPythonProject\\DownloadMusicFromYT\\sound\\1955.mp4")
#
# audio_clip.write_audiofile("example.mp3")

def convert(files):
    audio_files = os.listdir(files)
    for file in audio_files:
        # Получаем полный путь к файлу
        full_path = os.path.abspath(file)

        # Извлекаем имя файла (без пути)
        file_name = os.path.basename(full_path)
        full_path = f"C:\\Users\\horob\\NewPythonProject\\DownloadMusicFromYT\\sound\\{file_name}"

        # Создаем объект AudioFileClip
        audio_clip = AudioFileClip(full_path)

        # Создаем имя для MP3-файла
        mp3_file_name = os.path.splitext(file_name)[0] + '.mp3'

        # Получаем полный путь для сохранения MP3
        path_save = "C:\\Users\\horob\\NewPythonProject\\DownloadMusicFromYT\\convert"
        mp3_full_path = os.path.join(path_save, mp3_file_name)

        # Записываем аудио в MP3
        audio_clip.write_audiofile(mp3_full_path)


path = 'C:\\Users\\horob\\NewPythonProject\\DownloadMusicFromYT\\sound'
convert(path)
