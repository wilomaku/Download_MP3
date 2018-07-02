#! python3.5

from __future__ import unicode_literals
import subprocess, sys, bs4, requests, re, eyed3, youtube_dl, csv, glob

if len(sys.argv) > 1:
    # Get address from command line.
    savedir = ' '.join(sys.argv[1:])
    # TODO: Get address from clipboard.
else:
    # Get address from clipboard.
    #url_youtube = pyperclip.paste()
	savedir = input('Paste save path, including final /: ')

if savedir[-1] != '/':
	raise NameError('Save path should end up with /')

try:
	list_url = glob.glob('{}/*.csv'.format(savedir))[0]
except:
	raise NameError('URL list is not present, list should be csv file')

logfile_path = '{}log.txt'.format(savedir)
log = open(logfile_path, 'w')

with open(list_url, 'r') as f:
	reader = csv.reader(f)
	for url_obj in reader:
		url_youtube = url_obj[0]

		vid_youtube = requests.get(url_youtube)
		vid_youtube.raise_for_status()
		youtubeSoup = bs4.BeautifulSoup(vid_youtube.text, 'lxml')

		regexp = re.compile(r'[^\n]')
		title_song = youtubeSoup.select('h1')[1].getText()
		title_song = ''.join(regexp.findall(title_song)).strip()

		if 'ft.' in title_song:
			print('Downloading video')
			subprocess.call(['youtube-dl', '--add-metadata', '-o', '{}{}.webm'.format(savedir,title_song), '{}'.format(url_youtube)])
			print('Extracting audio')
			subprocess.call(['ffmpeg', '-i', '{}{}.webm'.format(savedir,title_song), '-vn', '-c:a', 'libmp3lame', '-qscale:a', '2', '-y', '{}{}.mp3'.format(savedir,title_song)])
			subprocess.call(['rm', '{}{}.webm'.format(savedir,title_song)])

			print('Tagging MP3')
			audiofile = eyed3.load('{}{}.mp3'.format(savedir,title_song))

			audiofile.tag.album = u'Postmodern Jukebox'
			audiofile.tag.album_artist = u'Postmodern Jukebox'
			regexp = re.compile(r'(.*) - ')
			audiofile.tag.title = regexp.findall(title_song)[0]
			audiofile.tag.artist = title_song.split('. ',1)[1]
			audiofile.tag.track_num = 1
			audiofile.tag.genre = 'Jazz Cover'
			audiofile.tag.save()
			print('MP3 sucessfully saved!')
		else:
			log.write(url_youtube)
			log.write('\n')
log.close()
