import os
import sys

import spacy
import nltk
from typing import *
from model import *
import csv
from wtpsplit import WtP


nlp = spacy.load("en_core_web_trf")
import en_core_web_trf

parser = en_core_web_trf.load()

nltk.download('stopwords')
nltk.download('punkt')
en_stop = set(nltk.corpus.stopwords.words('english'))
additional_en_stop = {"um", "uh", "yeah", "blah", "-", "[", "]"}
wtp = WtP("wtp-canine-s-12l")


def should_include(token: spacy.tokens.token.Token) -> bool:
    value = get_token_value(token)
    if len(value) < 2:
        return False
    if token.orth_.isspace():
        return False
    if value in en_stop:
        return False
    if value in additional_en_stop:
        return False
    return True


def get_token_value(token: spacy.tokens.token.Token) -> str:
    return token.lemma_.lower()


def tokenize(text: str) -> Iterator[str]:
    parser.max_length = len(text) + 100
    return (token.lemma_.lower() for token in parser(text) if should_include(token))


def read_transcripts(file: str) -> str:
    return " ".join(read_transcripts_lines(file))

def read_transcripts_lines(file: str) -> List[str]:
    with open(file, "r") as f:
        return f.read().splitlines()


def read_tokenized_transcripts(file: str) -> Iterator[str]:
    return tokenize(read_transcripts(file))

def read_tokenized_transcripts_lines(file: str) -> List[List[str]]:
    return [list(tokenize(line)) for line in read_transcripts_lines(file)]


def clean_transcripts(file: str):
    print(f"reading transcripts file {file}")
    with open(f"{file[:-4]}-cleaned.txt", "w") as f:
        for token in read_tokenized_transcripts(file):
            f.write(f"{token}{os.linesep}")
    print(f"transcripts file {file} was processed")


def read_dataset(file: str) -> List[DataSource]:
    with open(file, "r") as f:
        csv.field_size_limit(sys.maxsize)
        csvFile = csv.reader(f, delimiter=',', quotechar='"')
        next(csvFile, None)
        return [DataSource.from_csv_entry(line) for line in csvFile]

def texts_for_category(category: str, sources: List[DataSource]) -> Iterator[str]:
    return (source.text for source in sources if source.category == category)

def tokens_for_category(category: str, sources: List[DataSource]) -> Iterator[str]:
    for text in texts_for_category(category, sources):
        for token in tokenize(text):
            yield token


def sentences_for_category(category: str, sources: List[DataSource]) -> Iterator[str]:
    for source in sources:
        if source.category == category:
            return sentences(source.text, source.audio_to_speech)

def sentences(text: str, audio_to_speech: bool) -> Iterator[str]:
    if audio_to_speech:
        for sentence in nltk.sent_tokenize(text, language="english"):
            yield sentence
    else:
        for sentence in wtp.split(text, lang_code="en", style="ud", threshold=0.01):
            yield sentence


if __name__ == "__main__":
    for sentence in sentences_for_category("scientific-before", read_dataset("dataset.csv")):
        print(f"sentence length: {len(sentence)}")
