# Download_MP3
Script for extracting mp3 files from a given youtube channel

The 'extract_url' script extracts all possible url videos from a given channel. The 'download_mp3' script loads a CSV file witt an URL list. This scrip needs bs4 for extracting html elements, youtube_dl for downloading video and eyed3 for tagging mp3. The ffmpeg external library is mandatory too. mp3 files are not converted directly because youtube_dl generates a non-taggable file.

Refs:

bs4:[https://www.crummy.com/software/BeautifulSoup/bs4/doc/]

youtube_dl:[https://rg3.github.io/youtube-dl/download.html]

eyed3:[http://eyed3.readthedocs.io/en/latest/]

ffmpeg:[https://www.ffmpeg.org/download.html]
