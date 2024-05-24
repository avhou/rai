import json
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
    youtube_sources = ["scientific-before.txt", "scientific-after.txt", "non-scientific-before.txt",
                       "non-scientific-after.txt"]
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


def generate_sentences():
    print(f"generating sentence files")
    datasources = read_dataset("dataset.csv")
    for category in ["scientific-before", "scientific-after", "non-scientific-before", "non-scientific-after"]:
        num_sentences = 0
        with open(f"sentences-{category}.txt", "w") as f:
            for sentence in sentences_for_category(category, datasources):
                num_sentences += 1
                f.write(f"{sentence}{os.linesep}")
        print(f"wrote {num_sentences} sentences in file for category {category}")

    print("done")


def generate_annotated_sentences():
    print(f"generating annotated sentence files")
    datasources = read_dataset("dataset.csv")
    for category in ["scientific-before", "scientific-after", "non-scientific-before", "non-scientific-after"]:
        num_sentences = 0
        with open(f"sentences-annotated-{category}.csv", "w") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='"')
            writer.writerow(["category", "youtube", "num", "date", "audio-to-speech", "text"])
            for source in datasources:
                if source.category == category:
                    for sentence in sentences(source.text, source.audio_to_speech):
                        writer.writerow(
                            [category, source.youtube, str(source.num).zfill(3), source.date.strftime("%Y%m%d"),
                             source.audio_to_speech, sentence])
                        num_sentences += 1
        print(f"wrote {num_sentences} annotated sentences in file for category {category}")

    print("done")

def write_token_documents():
    # text = [["this", "is", "a", "sentence"], ["this", "is", "a", "second", "sentence"]]
    # print(text)
    # with open("test.txt", "w") as f:
    #    json.dump(text, f)
    # with open("test.txt", "r") as f:
    #     retrieved_texts = json.load(f)
    #     print(retrieved_texts)

    def write_tokens(category: str, kind: str, source: str):
        print(f"write tokens for category {category}, kind: {kind}, source: {source}")
        datasources = read_dataset("dataset.csv") if source == "full-text" else read_dataset(f"sentences-annotated-{category}.csv")
        with open(f"tokens-{category}-{kind}-{source}.txt", "w") as f:
            texts = [nltk.word_tokenize(datasource.text.lower()) for datasource in datasources if datasource.category == category] if kind == "no-preprocessing" else [list(tokenize(datasource.text)) for datasource in datasources if datasource.category == category]
            json.dump(texts, f)

    for category in ["scientific-before", "scientific-after", "non-scientific-before", "non-scientific-after"]:
        for kind in ["no-preprocessing", "preprocessing"]:
            for source in ["full-text", "sentences"]:
                write_tokens(category, kind, source)
    print(f"done")

if __name__ == "__main__":
    # prepare_data()
    # generate_sentences()
    # generate_annotated_sentences()
    write_token_documents()
