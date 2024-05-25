---
title: "IM0802-232434M - Responsible Artificial Intelligence assignment 2"
subtitle: "Pre and post ChatGPT Artificial General Intelligence topic and sentiment analysis"
author: "Alexander Van Hecke (852631385)"
abstract: "Artificial General Intelligence (AGI) has been a heavily debated topic for many years.  The introduction of ChatGPT was a milestone in the field of AI.  This research aims to extract and analyze transcripts from talks and interviews about AGI found on Youtube.  Both expert and non-expert opinions are considered and compared.  We analyze the discussed topics as well as the general sentiment (positive or negative).  We consider ethical issues such as safety concerning the use of AGI systems."
institute: "OU"
date: \today
geometry: margin=2.5cm
numbersections: false
link-citations: true
link-bibliography: true
papersize: a4
---

# Introduction

The field of Artificial Intelligence (AI) is vast.  Many different approaches to intelligence have been studied, including model based approaches, rule driven systems and data driven approaches (machine learning and deep neural engineering).  Many of these systems excel at certain tasks, sometimes surpassing human capabilities for these specific tasks.  Artificial General Intelligence (AGI) aims to be a kind of AI that matches or surpasses human capabilities across a wide range of cognitive tasks.

AGI has been debated for many years.  A model to compare AGI models is introduced in [@agi1].  An approach to create a library to contain the knowledge and datasets needed for AI models to learn is introduced in [@agi2].  These are technical approaches to achieve AGI.  

However, there are risks involved in achieving AGI, and this has been studied in depth as well.  A systematic review of risks associated with AGI is done in [@risks1].  The authors identify several risks, including AGIs with poor ethics, morals and values, and AGIs being given unsafe goals.  Several ethical issues and risks are described in [@risks2].  The authors discuss a wide variety of issues, such as the lack of trust, transparency, privacy, accountability and liability, the possible loss of human decision making, and unfairness.  

Not everyone is convinced AGI is possible.  There may be fundamental limitations to what an AGI can achieve.   The authors of [@limits1] argue that AI agents are limited in their ability to leverage new affordances.  According to the authors, an algorithmic approach as leveraged by AI agents is not able to generalize to unforeseen (or untrained) uses of an object, for example.  The authors of [@limits2] state AGI will never be achieved.  They acknowledge that the performance of special purpose AIs has been impressive in some cases, but claim we have not come much closer to AGI.

The introduction of ChatGPT [@chatgpt] on November 30, 2022 changed the narrative about AI.  Did OpenAI, the company behind ChatGPT, achieve AGI?  The authors of [@chatgpt1] investigate whether the technique of human-centric functional modeling (HCFM) can be used to provide a functional definition of intelligence that can be used to confirm whether ChatGPT can be classified as an AGI.  They conclude several HCFM criteria are not met.  The authors of [@chatgpt2] designate ChatGPT as an AGI.

In this paper we want to examine the opinions on AGI of both the scientific and the non-scientific community.  We use natural language processing (NLP) to analyze the transcripts of a collection of youtube videos, and try to compare the topics discussed and the sentiment about AGI in these communities both before and after the introduction of ChatGPT.

# Goal

In this paper, we aim to investigate whether the introduction of ChatGPT changed the topics discussed in the scientific and non-scientific community.  We formulate a first research question.

> **RQ 1 : Did the introduction of ChatGPT change the topics discussed in the scientific and non-scientific AGI community? **

Furthermore, we are interested in investigating whether sentiment about AGI has changed after the introduction of ChatGPT.   Risks related to AGI were already studied before the introduction of ChatGPT, but new questions were raised, e.g. the potential for abuse, the unjustified use of source datasets, copyright issues, and hallucination of results.  We formulate a second research question.

> **RQ 2 : Did the introduction of ChatGPT change the general sentiment about AGI in the scientific and non-scientific AGI community? **

To start off, we will look at the characteristics of the data used and discuss pre-processing steps.  Then, we will discuss design methodology and analyze the obtained results.  Finally, we will take into account some broader ethical issues such as safety.

# Data analysis

## Dataset description {#sec:dataset}

We used a manually curated list of Youtube videos as input for our analysis.  The list was created by Professor Clara Maathuis of the Open University [@ou] and included experts both from the scientific community and the non-scientific community.  Table \ref{table:experts} summarizes the experts included in the list.

| community      | experts                                                                                                                              |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| scientific     | Ben Goertzel, Ray Kurzweil, Nick Bostrom, Roman V. Yampolskiy, Ilya Sutskever, Yann LeCun, Yoshua Bengio, Andrej Karpathy, Andrew Ng |
| non-scientific | Elon Musk, Sam Altman, Mark Zuckerberg, Bill Gates                                                                                   |

Table:  Experts included \label{table:experts}


Several people had to be excluded from both communities as no videos were found before or after the introduction of ChatGPT.  Searches were done using both Youtube and Google Videos search.   Pei Wang, Cassio Pennachin, Ian Goodfellow and Yuval Noah Harari were excluded for this reason from the scientific community.  Other important voices in the non-scientific community such as Jef Bezos, Jack Ma and Chew Sho Zi were excluded as their opinions are less related to AGI. 


When available, the automatically generated transcripts from Youtube were used as input text.   However, these transcripts were not avaiable for all videos.  For these videos, we extracted the audio part of the videos and looked at speech-to-text solutions to extract the text from these audio fragments.  Several speech-to-text solutions are available, and we evaluated the `SpeechToRecognition` project [@speechrecognition] using the offline `Sphinx` engine.  However, this mostly produced nonsensical transcripts.  The transcripts generated by the (commercial) solution provided by AssemblyAI [@assemblyai] where evaluated manually and these results were of much higher quality.  A dataset containing all transcript text and some necessary metadata was created.  Table \ref{table:features} summarizes the features of the dataset.  Table \ref{table:counts} summarizes the number of documents and tokens in the scientific and non-scientific community, both before and after the introduction of ChatGPT.


| feature        | domain                                       | description                              |
|:---------------|----------------------------------------------|:-----------------------------------------|
| category       | {scientific, non-scientific}-{before, after} | The community the video belongs to       |
| youtube        | url                                          | The URL of the Youtube video             |
| num            | numeric                                      | The sequence number of the video         |
| date           | date                                         | The date the video was posted on Youtube |
| speech-to-text | boolean                                      | Text generated by speech-to-text?        |
| text           | string                                       | Transcript text                          |

Table:  Dataset features \label{table:features}

| community      | ChatGPT | number of documents | number of tokens |
|:---------------|---------|--------------------:|-----------------:|
| scientific     | before  |                  29 | 160.961          |
| scientific     | after   |                  28 | 138.561          |
| non-scientific | before  |                   6 | 25.355           |
| non-scientific | after   |                   7 | 29.788           |

    Table:  Documents and tokens per community \label{table:counts}

## Data pre-processing

Several pre-processing steps were performed before doing the actual analysis of the transcripts.  

Transcripts downloaded from Youtube are meant to be used as subtitles while watching the videos on Youtube.    They contain time indexes in order to show the right text at the right time, and may contain duplicate parts of a sentence as the video progresses in real time and the same part of a sentence may have to be shown for several time indexes.   Unfortunately, the use of these transcripts as subtitles also means very few (if any) punctuation marks are included.  After removal of time information and duplicate parts of sentences, we were left with a large blob of text (contiguous words) containing no sentence information.

Having sentences rather than a collection of contiguous words is important for sentiment analysis, so sentence determination was necessary.  For the transcripts downloaded from youtube, no punctutation marks were available and wtpsplit [@wtpsplit] with the `wtp-canine-s-12l` model was used to automatically generate sentences from the contiguous words.  For the transcripts generated by AssemblyAI [@assemblyai], punctuation marks were included and the sentence tokenizer of the Natural language toolkit (NLTK) [@nltk] was used.

The tokenization of sentences included several filters and transformations.  The spaCy [@spacy] `en_core_web_trf` was used to detected separate tokens, and tokens were excluded if they were of length 1, consisted only of whitespace (e.g. tabs, newlines, spaces), were in the NLTK [@nltk] English stopword list, or were in an additonal, manually curated stopword list.   This additional stopword list was necessary as the transcripts contained a lot of filler words like 'uh', 'um' and 'yeah' and these showed up in the most frequently used words.   Finally, all tokens were lemmatized.

Table \ref{table:pre-processing} summarized the different pre-processing steps.

| step                         | technology                        | description                                                                                            |
|:-----------------------------|-----------------------------------|:-------------------------------------------------------------------------------------------------------|
| cleanup youtube transcripts  | Python                            | Remove time indexes, remove duplicate parts of sentences                                               |
| sentence determination       | wtsplit [@wtpsplit], NLTK [@nltk] | Split larger texts in coherent sentences                                                               |
| tokenization filters         | spaCy [@spacy], NLTK [@nltk]      | Remove small tokens, stopwords, filler words ("um", "uh", "yeah", "blah", "-", "[", "]"), whitespaces. |
| tokenization transformations | spaCy [@spacy]                    | Lemmatization of tokens                                                                                |

Table:  Dataset features \label{table:pre-processing}


# Methodology and Implementation

## Research methodology and design

We performed different analyses on the pre-processed data.

Wordclouds are a simple and visual tool to highlight important (often used) words in a collection of texts.  It visualizes the most frequently used words, varying the fontsize of words to indicate relative importance of the word in the cloud.  Separate wordclouds were generated for the pre-processed data of the scientific and non-scientific community, both before and after the introduction of ChatGPT.

An N-gram analysis (bigrams and trigrams) was performed on the pre-processed data.  N-grams give a general idea about the kinds of expressions often used in texts, and are a simple means to try to detect important subjects in texts.  Data was split in four groups (scientific community before ChatGPT, scientific community after ChatGPT, non-scientific community before ChatGPT, non-scientific community after ChatGPT) and was fed to N-gram (N=2,3) NLTK [@nltk] models.  

The GenSim framework [@gensim] was used for a topic modeling analysis.  A Latent Dirichlet Allocation (LDA) model was trained on four tokenized and pre-processed documents (containing all tokens of scientific/non-scientific - before ChatGPT/after ChatGPT texts).  The model was asked to generate 100 possible topics, each containing 10 words.  The 6 most important topics, as determined by the heighest weight of the first word of the topic, were kept and visualised.

Finally, a sentiment analysis was performed using the Flair framework [@flair].  Since the goal was to visualize the possible change of average sentiment over time, we split the transcripts in 2 groups (scientific and non-scientific).  For each transcript in each group, sentences were generated and fed to the flair `sentiment` Classifier.   This yielded a score between 0 and 1 and a label (POSITIVE or NEGATIVE) for each sentence.  A positive score was kept as is, and a negative score was multiplied by -1 to yield a value between -1 and 0.  These corrected score were averaged per transcript, yielding a date (the date the Youtube video was uploaded) and an average sentiment score.  Repeating this procedure for all transcripts in both groups allowed us to visualize the possible change of sentiment towards AGI in the scientific and non-scientific community. 

## Implementation

All code and data is available in a github repository [@github].  We recap the most important files here : 

- `srt_to_txt.py` contains the code to transform srt subtitle transcripts as download from youtube to contiguous words
- `utils.py` contains several utility methods to load transcripts and their metadata, to iterate over tokens of transcripts, etc
- `prepare_data.py` contains a script to pre-generate input data used in the jupyter notebooks (e.g. tokenized sentences for all transcripts of a community before or after the introduction of ChatGPT)
- `wordcloud.ipynb` is a jupyter notebook that performs the wordcloud analysis
- `ngrams.ipynb` is a jupyter notebook that performs the N-gram analysis
- `topic.ipynb` is a jupyter notebook that performs the topic modeling analysis
- `sentiment_analysis.ipynb` is a jupyter notebook that performs the sentiment analysis

# Evaluation and Results

## RQ 1

In order to evaluate RQ 1, we look at the results of the wordcloud, N-gram and topic modeling analysis.  

Figures @{fig:wordcloud-scientific-before} and @{fig:wordcloud-scientific-after} illustrate the most important words of discussions in the scientific community before and after the introduction of ChatGPT.  A lot of words overlap between these two groups of transcripts.  The transcripts before ChatGPT seem to be mostly positive (good, human, people, right), whereas the transcripts after ChatGPT contain more negative words (problem, different, change).

![Wordcloud (scientific community before ChatGPT)](figures/wordcloud-scientific-before.png){#fig:wordcloud-scientific-before height=50% width=50%}

![Wordcloud (scientific community after ChatGPT)](figures/wordcloud-scientific-after.png){#fig:wordcloud-scientific-after height=50% width=50%}


Figures @{fig:wordcloud-non-scientific-before} and @{fig:wordcloud-non-scientific-after} illustrate the most important words of discussions in the non-scientific community before and after the introduction of ChatGPT.  We see the same pattern as in the scientific community.  The discussions after ChatGPT seem to contain more negative words (problem, bad, hard).

![Wordcloud (non-scientific community before ChatGPT)](figures/wordcloud-non-scientific-before.png){#fig:wordcloud-non-scientific-before height=50% width=50%}

![Wordcloud (non-scientific community after ChatGPT)](figures/wordcloud-non-scientific-after.png){#fig:wordcloud-non-scientific-after height=50% width=50%}

Bigrams are a very simple and limited language model.  Nevertheless, we see interesting patterns arise in bigram data for the scientific community, see Figure @{fig:bigrams}.  The conversation seems to have shifted from machine learning and deep learning (before ChatGPT) to large language models (LMM) and super intelligence (after ChatGPT).  We do not see the same shift for the non-scientific community, where the bigrams do not seem to contain any useful information.   Of note however is that OpenAI is one of the top 10 bigrams after the introduction of ChatGPT.

![Bigrams](figures/ngram-bigrams.png){#fig:bigrams}

Trigrams (see Figure @{fig:trigrams}) should be able to capture a bit more context than bigrams.  In the scientific community, we see focus shift from traditional techniques like deep neural nets and self supervised learning before ChatGPT to large language models after ChatGPT.   There seems to more attention on human level intelligence and AI.  The non-scientific community seems to shift towards a more negative vision after the introduction of ChatGPT, as evidenced by the mention of "brave new world" and "world war iii".

![Trigrams](figures/ngram-trigrams.png){#fig:trigrams}


Figures @{fig:topic-modeling-scientific-before} and @{fig:topic-modeling-scientific-after} illustrate the 6 most important topics determined by an LDA model for the scientific community.  Few relevant topics seem to have been extracted by the model.  Topic 6 of the scientific community before ChatGPT seems to point in the direction of possible problems with AGI, and topic 3 of the scientific community after ChatGPT seems to be about super intelligence, but few conclusions can be drawn from these results.

![Topic modeling (scientific community before ChatGPT)](figures/topic-modeling-scientific-before.png){#fig:topic-modeling-scientific-before}

![Topic modeling (scientific community after ChatGPT)](figures/topic-modeling-scientific-after.png){#fig:topic-modeling-scientific-after}

Figures @{fig:topic-modeling-non-scientific-before} and @{fig:topic-modeling-non-scientific-after} illustrate the 6 most important topics determined by an LDA model for the non-scientific community.  Here, the focus seems to have shifted from topics about climate change (Topic 4) and (super)human-level intelligence (Topic 6) before ChatGPT to discussions about the replacement of workforce by AGI (Topic 1) and a breakthrough accomplished by the GPT-4 model (Topic 3) after ChatGPT.  

It appears an LDA model was not able to capture many relevant topics given the (very) limited dataset we used.  It would be interesting to see if this can be improved by feeding it more data.

![Topic modeling (non-scientific community before ChatGPT)](figures/topic-modeling-non-scientific-before.png){#fig:topic-modeling-non-scientific-before}

![Topic modeling (non-scientific community after ChatGPT)](figures/topic-modeling-non-scientific-after.png){#fig:topic-modeling-non-scientific-after}

## RQ 2



# Discussion

zeker te vermelden : weinig data non-scientific.   interessant om te doen met meer data

# Conclusions

zeker te vermelden : weinig data non-scientific.   interessant om te doen met meer data

# References

::: {#refs}
:::
