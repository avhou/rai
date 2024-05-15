#!/bin/bash

rm -rf scientific-before
rm -rf scientific-after
rm -rf non-scientific-before
rm -rf non-scientific-after

mkdir scientific-before
mkdir scientific-after
mkdir non-scientific-before
mkdir non-scientific-after

yt-dlp --write-auto-sub --convert-subs srt -x --audio-format mp3 -o "scientific-before/%(autonumber)03d-%(upload_date)s-.%(ext)s" -a scientific-before.txt
yt-dlp --write-auto-sub --convert-subs srt -x --audio-format mp3 -o "scientific-after/%(autonumber)03d-%(upload_date)s-.%(ext)s" -a scientific-after.txt
yt-dlp --write-auto-sub --convert-subs srt -x --audio-format mp3 -o "non-scientific-before/%(autonumber)03d-%(upload_date)s-.%(ext)s" -a non-scientific-before.txt
yt-dlp --write-auto-sub --convert-subs srt -x --audio-format mp3 -o "non-scientific-after/%(autonumber)03d-%(upload_date)s-.%(ext)s" -a non-scientific-after.txt

cp scientific-before-audio-to-text/*.txt scientific-before
cp non-scientific-before-audio-to-text/*.txt scientific-before

python3 srt_to_txt.py scientific-before/*.srt
cat scientific-before/*.txt | uniq > scientific-before/transcripts.txt

python3 srt_to_txt.py scientific-after/*.srt
cat scientific-after/*.txt | uniq > scientific-after/transcripts.txt

python3 srt_to_txt.py non-scientific-before/*.srt
cat non-scientific-before/*.txt | uniq > non-scientific-before/transcripts.txt

python3 srt_to_txt.py non-scientific-after/*.srt
cat non-scientific-after/*.txt | uniq > non-scientific-after/transcripts.txt

