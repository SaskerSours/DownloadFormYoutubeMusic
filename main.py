from getLink import getLinks
from download import download_video
play = 'https://www.youtube.com/playlist?list=PLSRu2f7nOQmcnZL3SJaLMtP9ROeqXZUb3'


def main(playlist_link):
    links = []
    links = getLinks(playlist_link)
    download_video(links)


main(play)
