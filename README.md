# SRT fixer

Fixes overlapping timestamps in SRT files by merging the entries.
This is useful after converting ASS files to SRT.

[![Build Status](https://travis-ci.org/ThomasHertleif/srt-fixer.svg?branch=master)](https://travis-ci.org/ThomasHertleif/srt-fixer)

## Usage 

```sh
$ git clone git@github.com:ThomasHertleif/srt-fixer.git
$ cd srt-fixer
$ python main.py $PATH_TO_SRT_FILE -o $PATH_TO_OUTPUT_FILE
```
## Example SRT

### Input SRT

```
1
00:00:03,100 --> 00:00:03,560
foo

2
00:00:03,400 --> 00:00:03,800
bar
```

### Output SRT
```
1
00:00:03,100 --> 00:00:03,800
foo
bar
```