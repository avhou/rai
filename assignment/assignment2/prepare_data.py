from typing import *
import csv
import os
import re
from utils import *
from nltk.tokenize import sent_tokenize
from wtpsplit import WtP

wtp = WtP("wtp-canine-s-12l")
# for sentence in wtp.split(content, lang_code="en"):

def source_enumeration(source: str) -> List[Tuple[str, int]]:
    with open(source, 'r') as f:
        lines = f.read().splitlines()
        return [(source, num) for (num, source) in enumerate(lines, start=1)]


def deduplicate(file: str) -> Tuple[bool, str]:
    previous_line = None
    results = []
    num_lines = 0
    for line in read_transcripts_lines(file):
        if line != previous_line:
            results.append(line)
        previous_line = line
        num_lines += 1
    return (num_lines > 1, " ".join(results))


def prepare_data():
    print(f"preparing data")
    pattern = re.compile(r"(\d{3})-(.*)-(.*)")
    youtube_sources = ["scientific-before.txt", "scientific-after.txt", "non-scientific-before.txt", "non-scientific-after.txt"]
    folders = ["scientific-before", "scientific-after", "non-scientific-before", "non-scientific-after"]
    with open("dataset.csv", "w") as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        writer.writerow(["category", "youtube", "num", "date", "audio-to-speech", "text"])
        for (youtube_source, folder) in zip(youtube_sources, folders):
            print(f"checking youtube source: {youtube_source} in folder {folder}")
            text_files = [file for file in os.listdir(folder) if file.endswith(".txt")]
            for (video, num) in source_enumeration(youtube_source):
                matches = [file for file in text_files if file.startswith(str(num).zfill(3))]
                date = "unknown"
                content = "unknown"
                has_many_lines = True
                if len(matches) == 1:
                    match = re.search(pattern, matches[0])
                    if match:
                       date = match.groups()[1]
                    (has_many_lines, content) = deduplicate(os.path.join(folder, matches[0]))
                else:
                    print(f"could not find video with num {num} in folder {folder} (source {youtube_source})!")
                writer.writerow([folder, video, str(num).zfill(3), date, not has_many_lines, content])

    print("done")

if __name__ == "__main__":
    prepare_data()
