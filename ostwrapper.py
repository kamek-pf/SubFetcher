import xmlrpc.client
import urllib.request
import gzip
from localvideo import LocalVideo

# OpenSubtitles wrapper
class OpenSubtitleWrapper:

	def __init__(self):
		self.ost = xmlrpc.client.ServerProxy("http://api.opensubtitles.org/xml-rpc")
		self.url = 'No subtitles available'

	# Log into OpenSubtitles
	# Returns a login token needed by XMLRPC
	def login(self):
		login = self.ost.LogIn("", "", "en", "OSTestUserAgent")
		self.token = login['token']
		return login['status']

	# Logout when we're done
	def logout(self):
		logout = self.ost.LogOut(self.token)
		return logout['status']

	# Find subtitles matching the file name
	# Returns the appropriate download URL
	def findSubtitleFor(self, localVideo):
		searchParams = [{'tag': localVideo.name, 'sublanguageid': 'eng'}]
		subtitleQuery = self.ost.SearchSubtitles(self.token, searchParams) 

		if subtitleQuery['data']:
		        self.url = subtitleQuery['data'][0]['SubDownloadLink'] 
		        return self.url

	# Download the subtitles found by previous method
	# Subtitles are gziped, so gunzip them here
	# TODO : delete the archive afterwards
	def downloadSubtitle(self, localVideo):
		if (self.url != 'No subtitles available'):
		        localSrt = localVideo.dirname + '/' + localVideo.noExtName + '.srt'
		        localArchive = localSrt + '.gz'

		        urllib.request.urlretrieve(self.url, localArchive)

		        with gzip.open(localArchive, 'rb') as f:
		        	archiveContent = f.read()
		        f.close()

		        with open(localSrt, 'w') as s:
		        	s.write(str(archiveContent, 'UTF-8'))
		        s.close()

		        return 'Nothing was downloaded'
		else: 
		        return 'Subtitle downloaded successfuly'

	# Main method
	# Fetch subtitle from file name
	def fetchSubtitlesFor(self, localVideo):
		self.login()
		self.findSubtitleFor(localVideo)
		self.downloadSubtitle(localVideo)
		self.logout()


