import os

import spacy
import nltk
from typing import *

nlp = spacy.load("en_core_web_trf")
import en_core_web_trf

parser = en_core_web_trf.load()

nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
additional_en_stop = {"um", "uh", "-", "[", "]"}


def should_include(token: spacy.tokens.token.Token) -> bool:
    value = get_token_value(token)
    if token.orth_.isspace():
        return False
    if value in en_stop:
        return False
    if value in additional_en_stop:
        return False
    if len(value) < 2:
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


def clean_transcripts(file: str):
    print(f"reading transcripts file {file}")
    with open(f"{file[:-4]}-cleaned.txt", "w") as f:
        for token in read_tokenized_transcripts(file):
            f.write(f"{token}{os.linesep}")
    print(f"transcripts file {file} was processed")


if __name__ == "__main__":
    import nltk
    from nltk import bigrams
    from nltk import trigrams

    tokens = list(read_transcripts_lines("scientific-after/transcripts-cleaned.txt"))
    bi_tokens = bigrams(tokens)
    tri_tokens = trigrams(tokens)

    fdist = nltk.FreqDist(bi_tokens)
    for k,v in sorted(fdist.items(), key=lambda x:int(x[1]), reverse=True)[:10]:
        print(k, v)
