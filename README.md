## Description :

An OpenSubtitles wrapper written in Python 3.

This is used to grab the subtitles of a video using the XMLRPC API provided by OpenSubtitles.
I'll probably use this to make a plugin for mpv, as I miss the ability to easily download subtitles since I switched from SMPlayer.
Subfetcher will download english subtitles matching your file.
Other languages aren't supported yet.

## Install :

Arch users can install the package 'subfetcher-git' from the AUR.

```
packer -S subfetcher-git
```

If you're not using Arch :

```
python setup.py install
```

## Usage :

```
subfetcher /path/to/your/video.ext
```
