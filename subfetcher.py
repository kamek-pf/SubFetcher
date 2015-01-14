from localvideo import LocalVideo
from ostwrapper import OpenSubtitleWrapper

# Temporary test file, this will be replaced by a propper main file

# Open local file
path = "/home/kamek/Downloads/Penny.Dreadful.S01E03.720p.HDTV.x264-KILLERS[rarbg]/penny.dreadful.s01e03.720p.hdtv.x264-killers.mkv"
localVideo = LocalVideo(path)

# Get the subtitles for that file
ost = OpenSubtitleWrapper()
ost.fetchSubtitlesFor(localVideo)