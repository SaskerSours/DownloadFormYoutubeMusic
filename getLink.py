import re
import requests

headers = {
    'Accept': "*/*",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    'x-youtube-client-name': '1',
    'x-youtube-client-version': '2.20200529.02.01',
    'X-Content-Type-Options': 'nosniff',
    'X-Xss-Protection': '1',

}


def getLinks(url):
    base_link = 'https://www.youtube.com/watch?v='
    req = requests.get(url, headers=headers)
    src = req.text

    # Используем регулярное выражение для извлечения ссылок
    pattern = re.compile(r'"url":"/watch\?v=([^"]+)')
    matches = pattern.findall(src)

    unique_links = set()  # Создаем пустое множество для уникальных ссылок

    for match in matches:
        cut = match.split('\\')
        unique_links.add(cut[0])  # Добавляем уникальные ссылки во множество
    full_links = [base_link + code for code in list(unique_links)]

    return full_links  # Возвращаем уникальные ссылки в виде списка

