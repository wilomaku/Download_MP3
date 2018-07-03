# Download_MP3
Script to download mp3 from youtube video

Scrit loads a CSV file witt URL list. This scrip needs bs4 for extract html elements, youtube_dl for download video and eyed3 for tag mp3. ffmpeg external library is mandatory too. MP3 is not converted directly because youtube_dl generates a not taggable file.

Refs:

bs4:[https://www.crummy.com/software/BeautifulSoup/bs4/doc/]

youtube_dl:[https://rg3.github.io/youtube-dl/download.html]

eyed3:[http://eyed3.readthedocs.io/en/latest/]

ffmpeg:[https://www.ffmpeg.org/download.html]
