import requests
import io

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0',
#     'Accept': 'application/json',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'uuid': '0eca85718481000570a2e3cd05ec510c',
#     'Origin': 'https://ytmp3.cc',
#     'Connection': 'keep-alive',
#     'Referer': 'https://ytmp3.cc/',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'cross-site',
# }
#
# data = 'u=https://www.youtube.com/watch?v=61ymOWwOwuk&c=UA'
#
# response = requests.post('https://ytpp3.com/newp', headers=headers, data=data)
#
# # print(response.text)
#
# file_path = "output.mp3"
#
# if response.status_code == 200:
#     with open(file_path, "wb") as mp3_file:
#         mp3_file.write(response.content)
#     print("MP3 file saved successfully.")
# else:
#     print(f"Failed to retrieve the MP3. Status code: {response.status_code}")
import pytube


def download_video(links):
    for link in links:
        video = pytube.YouTube(link)
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_stream.download('sound')


linkk = ['https://www.youtube.com/watch?v=1B4AxahyQJQ', 'https://www.youtube.com/watch?v=MiAoetOXKcY',
         'https://www.youtube.com/watch?v=vAILCOvgF7s', 'https://www.youtube.com/watch?v=IuY54A3bOmg',
         'https://www.youtube.com/watch?v=BnnbP7pCIvQ', 'https://www.youtube.com/watch?v=TdrL3QxjyVw',
         'https://www.youtube.com/watch?v=-Ubyt7iWJ8Q', 'https://www.youtube.com/watch?v=1zjlqjr0TvQ',
         'https://www.youtube.com/watch?v=MD8flUkymrM', 'https://www.youtube.com/watch?v=veEG6flpfTo',
         'https://www.youtube.com/watch?v=CFjqZpZZ5jI']

lol = download_video(linkk)

print(lol)
#
