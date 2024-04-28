#!/bin/bash

rm -f scientific-before
rm -f scientific-after
rm -f non-scientific-before
rm -f non-scientific-after

mkdir scientific-before
mkdir scientific-after
mkdir non-scientific-before
mkdir non-scientific-after

yt-dlp --write-auto-sub --convert-subs srt --skip-download -o "scientific-before/%(autonumber)03d.%(ext)s" -a scientific-before.txt
yt-dlp --write-auto-sub --convert-subs srt --skip-download -o "scientific-after/%(autonumber)03d.%(ext)s" -a scientific-after.txt
yt-dlp --write-auto-sub --convert-subs srt --skip-download -o "non-scientific-before/%(autonumber)03d.%(ext)s" -a non-scientific-before.txt
yt-dlp --write-auto-sub --convert-subs srt --skip-download -o "non-scientific-after/%(autonumber)03d.%(ext)s" -a non-scientific-after.txt

python3 srt_to_txt.py scientific-before/*.srt
cat scientific-before/*.txt | uniq > scientific-before/transcripts.txt

python3 srt_to_txt.py scientific-after/*.srt
cat scientific-after/*.txt | uniq > scientific-after/transcripts.txt

python3 srt_to_txt.py non-scientific-before/*.srt
cat non-scientific-before/*.txt | uniq > non-scientific-before/transcripts.txt

python3 srt_to_txt.py non-scientific-after/*.srt
cat non-scientific-after/*.txt | uniq > non-scientific-after/transcripts.txt

