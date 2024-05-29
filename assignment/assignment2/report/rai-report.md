---
wtitle: "IM0802-232434M - Responsible Artificial Intelligence assignment 2"
subtitle: "Pre and post ChatGPT Artificial General Intelligence topic and sentiment analysis"
author: "Alexander Van Hecke (852631385)"
abstract: "Artificial General Intelligence (AGI) has been a heavily debated topic for many years.  The introduction of ChatGPT was a milestone in the field of AI.   This report aims to extract and analyze transcripts from talks and interviews about AGI found on Youtube.  Both expert and non-expert opinions are considered and compared.  We analyze the discussed topics as well as the general sentiment (positive or negative).  We consider ethical issues concerning the safe use of AGI systems."
institute: "OU"
date: \today
geometry: margin=2.5cm
numbersections: false
link-citations: true
link-bibliography: true
papersize: a4
---

# Introduction

The field of Artificial Intelligence (AI) is vast.  Many different approaches to intelligence have been studied, including model based approaches, rule driven systems and data driven approaches.  Many of these systems excel at certain tasks, sometimes surpassing human capabilities for these specific tasks.  Artificial General Intelligence (AGI) aims to be a kind of AI that matches or surpasses human capabilities across a wide range of cognitive tasks.

AGI has been debated for many years.  A model to compare AGI models is introduced in [@agi1].  An approach to create a library to contain the knowledge and datasets needed for AI models to learn is introduced in [@agi2].  These are technical approaches to achieve AGI.  

Not everyone is convinced AGI is possible.  There may be fundamental limitations to what an AGI can achieve.   The authors of [@limits1] argue that AI agents are limited in their ability to leverage new affordances.  According to the authors, an algorithmic approach as used by AI agents is not able to generalize to unforeseen (or untrained) situations.  The authors of [@limits2] state AGI will never be achieved.  They acknowledge that the performance of special purpose AIs has been impressive in some cases, but claim we have not come much closer to AGI.

There are risks involved in achieving AGI, and this has been studied in depth as well.  A systematic review of risks associated with AGI is done in [@risks1].  The authors identify several risks, including AGIs with poor ethics, morals and values, and AGIs being given unsafe goals.  Several ethical issues and risks are described in [@risks2].  The authors discuss a wide variety of issues, such as the lack of trust, transparency, privacy, accountability and liability, the possible loss of human decision making, and unfairness.  

The introduction of ChatGPT [@chatgpt] on November 30, 2022 changed discussions about AGI.  Did OpenAI, the company behind ChatGPT, achieve AGI?  The authors of [@chatgpt1] investigate whether the technique of human-centric functional modeling (HCFM) can be used to provide a functional definition of intelligence that can be used to confirm whether ChatGPT can be classified as an AGI.  They conclude several HCFM criteria are not met.  The authors of [@chatgpt2] designate ChatGPT as an AGI.

Irrespective of whether ChatGPT is an AGI or not, people soon started to reflect on the many ethical issues associated with generative AI in general and ChatGPT in particular.  We saw more discussions about the fear of super human level intelligence and humanity losing control to superior AI systems.  Competitors of OpenAI even suggested development of ChatGPT models should be temporarily suspended.  

We categorize an AGI system as **safe** when it acts ethically and responsibly, it complies with instructions and it resists bias.  Many aspects are important in this discussion :  

- **Copyright issues** : ChatGPT may have been trained on copyrighted materials.  What about the copyrights of the original authors who see their copyrighted material being made available to the public without proper compensation?
- **Transparency** : It is not clear how and why ChatGPT generates a response, which sources were used, or why it preferred one source over another.
- **Accountability** : Who is liable when ChatGPT produces false information and this leads to injury or other harm?
- **Data privacy** : People interact with ChatGPT by inputting prompts and they may give away personal information by doing so.  Data entered by users is used to further enhance the model, meaning people should not give away sensitive information.
- **Trust** : People may put too much trust in ChatGPT, not recognizing that it remains a statistical model.  ChatGPT very confidently hallucinates answers, meaning these answers cannot be trusted to be accurate.
- **Fairness**: ChatGPT is operated by OpenAI, which is (now) a commercial entity.  AGI should be available to all, not only to people who can afford monthly subscriptions.  Note there is a (limited) free layer.
- **Resilience and security**: AI systems need to be resilient and secure. In order to be safe, they need a fallback plan in case something goes wrong.  In order to minimize and prevent unintentional harm, they need to be accurate, reliable and reproducible.
- **Cybersecurity**: ChatGPT can be used to write very convincing texts, with the potential for abuse.  I.e. phishing emails and fake websites can be made with very little effort and these can be used to scam people.
- **Regulation**:  Some parts of the world have introduced AI regulation (EU AI act), but other parts of the world are still working on this.  To properly regulate global players like OpenAI, we need a global framework.  Given the rapid evolution of AI, this legal framework needs to be flexible enough to keep up with changing reality.
- **Input bias** : ChatGPT is trained on a huge internet corpus.  This data may be biased and as such, ChatGPT will learn these biases while being trained.
- **Instruction Compliance** : ChatGPT is a black box.  There is no reason to assume ChatGPT would deliberately generate text that defies instructions specified in the input prompts, but since it lacks real **transparency**, there is no way to know for sure whether commercial or other interests are preferred over user instructions.
- **Environmental impact**:  generative AI models have huge computational costs to both train and operate them.  This has a negative impact on the enviroment, which will only increase linearly with the use of such models.
- **Societal impact**: Finally, generative AI models may have a considerable impact on society as a whole, as it will become increasingly difficult to judge what information is human-made, correct and trustworthy.  Additionally, AGIs may have a profound impact on some professions.

In this report we aim to examine opinions on AGI of both the scientific and the non-scientific community.  These opinions are used as a proxy to determine whether experts estimate ChatGPT is safe to use in the sense described above.   We use natural language processing (NLP) to analyze the transcripts of a collection of Youtube videos, and try to compare the topics discussed and the sentiment about AGI in these communities both before and after the introduction of ChatGPT.  In particular, we will examine whether opinions on the safety of AGI systems have changed over time.

# Goal

In this report, we aim to investigate whether the discussion about safety of AGI systems has changed after the introduction of ChatGPT.  We use expert opinions in Youtube interviews and videos as a proxy to determine which AGI related topics are being discussed, and whether the general sentiment about AGI has changed after the introduction of ChatGPT.  In order to investigate this, we formulate 2 research questions.

The first research question will examine whether a shift in discussed topics can be detected.

> **RQ 1 : Did the introduction of ChatGPT change the topics discussed in the scientific and non-scientific AGI community? **

The second research question will examine whether a shift in sentiment in discussed topics can be detected.

> **RQ 2 : Did the introduction of ChatGPT change the general sentiment about AGI in the scientific and non-scientific AGI community? **

To start off, we will look at the characteristics of the data used and discuss pre-processing steps.  Then, we will discuss design methodology and analyze and discuss the obtained results.

# Data analysis

## Dataset description {#sec:dataset}

We used a manually curated list of Youtube videos as input for our analysis.  The list was created by Professor Clara Maathuis of the Open University [@ou] and included experts from both the scientific and the non-scientific community.  Table \ref{table:experts} summarizes the experts included in the list.

| community      | experts                                                                                                                              |
|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| scientific     | Ben Goertzel, Ray Kurzweil, Nick Bostrom, Roman V. Yampolskiy, Ilya Sutskever, Yann LeCun, Yoshua Bengio, Andrej Karpathy, Andrew Ng |
| non-scientific | Elon Musk, Sam Altman, Mark Zuckerberg, Bill Gates                                                                                   |

Table:  Experts included \label{table:experts}


Several people had to be excluded as no videos were found either before or after the introduction of ChatGPT.  Searches were done using both Youtube and Google Videos search.   Pei Wang, Cassio Pennachin, Ian Goodfellow and Yuval Noah Harari were excluded for this reason from the scientific community.  Other important voices in the non-scientific community such as Jef Bezos, Jack Ma and Chew Sho Zi were excluded as their opinions are less related to AGI. 


When available, the automatically generated transcripts from Youtube were used as input text.   However, these transcripts were not available for all videos.  For videos lacking transcripts, we extracted the audio part of the videos and looked at speech-to-text solutions to extract the text from these audio fragments.  Several speech-to-text solutions are available, and we evaluated the `SpeechToRecognition` project [@speechrecognition] using the offline `Sphinx` engine.  However, this produced mostly nonsensical transcripts.  The transcripts generated by the (commercial) solution provided by AssemblyAI [@assemblyai] were evaluated manually and judged to be of much higher quality.  A dataset containing all transcript text and metadata was created.  Table \ref{table:features} summarizes the features of the dataset.  Table \ref{table:counts} summarizes the number of documents and tokens in the scientific and non-scientific community, both before and after the introduction of ChatGPT.


| feature        | domain                                       | description                                    |
|:---------------|----------------------------------------------|:-----------------------------------------------|
| category       | {scientific, non-scientific}-{before, after} | Community + indication before or after ChatGPT |
| youtube        | url                                          | The URL of the Youtube video                   |
| date           | date                                         | The date the video was posted on Youtube       |
| speech-to-text | boolean                                      | Text generated by speech-to-text?              |
| text           | string                                       | Transcript text                                |

Table:  Dataset features \label{table:features}

| community      | ChatGPT | number of documents | number of tokens |
|:---------------|---------|--------------------:|-----------------:|
| scientific     | before  |                  29 | 160.961          |
| scientific     | after   |                  28 | 138.561          |
| non-scientific | before  |                   6 | 25.355           |
| non-scientific | after   |                   7 | 29.788           |

Table:  Documents and tokens per community \label{table:counts}

## Data pre-processing

Several pre-processing steps were performed.

Transcripts downloaded from Youtube are meant to be used as subtitles while watching the videos on Youtube.    They contain time indexes in order to show the right text at the right time, and may contain duplicate parts of a sentence as the video progresses in real time.   The origin of these transcripts as subtitles also means no punctuation marks are included.  After removal of time information and duplicate parts of sentences, we were left with a large blob of text (contiguous words) containing no sentence information.

Having sentences rather than a collection of contiguous words is important for sentiment analysis, so sentence determination was necessary.  For the transcripts downloaded from Youtube, wtpsplit [@wtpsplit] with the `wtp-canine-s-12l` model was used to automatically generate sentences from the contiguous words.  Transcripts generated by AssemblyAI [@assemblyai] included punctuation marks, and the sentence tokenizer of the Natural language toolkit (NLTK) [@nltk] was used.

The tokenization of sentences was done using several filters and transformations.  The spaCy [@spacy] `en_core_web_trf` was used to detected separate tokens, and tokens were excluded if they were of length 1, consisted only of whitespace (e.g. tabs, newlines, spaces), were in the NLTK [@nltk] English stopword list, or were in an additonal, manually curated stopword list.   This additional stopword list was necessary as the transcripts contained a lot of filler words like 'uh', 'um' and 'yeah' and these showed up in the most frequently used words.   Finally, all tokens were lemmatized.

Table \ref{table:pre-processing} summarizes the different pre-processing steps.

| step                         | technology                        | description                                                                             |
|:-----------------------------|-----------------------------------|:----------------------------------------------------------------------------------------|
| cleanup Youtube transcripts  | Python                            | Remove time indexes, remove duplicate parts of sentences                                |
| sentence determination       | wtsplit [@wtpsplit], NLTK [@nltk] | Split larger texts in coherent sentences                                                |
| tokenization filters         | spaCy [@spacy], NLTK [@nltk]      | Remove small tokens, stopwords, filler words ("um", "uh", "yeah", "blah"), whitespaces. |
| tokenization transformations | spaCy [@spacy]                    | Lemmatization of tokens                                                                 |

Table:  Dataset features \label{table:pre-processing}


# Methodology and Implementation

## Research methodology and design

We performed different analyses on the pre-processed data.

Wordclouds are a simple and visual tool to highlight important (often used) words in a collection of texts.  It visualizes the most frequently used words, varying the fontsize of words to indicate relative importance of the word in the cloud.  Separate wordclouds were generated for the data of the scientific and non-scientific community, both before and after the introduction of ChatGPT.

An N-gram analysis (bigrams and trigrams) was performed on the pre-processed data.  N-grams give a general idea about the kinds of expressions often used in texts, and are a simple means to try to detect important subjects in texts.  Data was split in four groups (scientific and non-scientific community before and after ChatGPT) and was fed to N-gram (N=2,3) NLTK [@nltk] models.  The 10 most frequently used N-grams were visualised.

The GenSim framework [@gensim] was used for a topic modeling analysis.  A Latent Dirichlet Allocation (LDA) model was trained on four tokenized and pre-processed documents (containing all tokens of scientific/non-scientific - before/after ChatGPT texts).  The model was asked to generate 100 possible topics, each containing 10 words.  The 6 most important topics, as determined by the heighest weight of the first word of the topic, were kept and visualised.

Finally, a sentiment analysis was performed using the Flair framework [@flair].  Since the goal was to visualize the possible change of average sentiment over time, we split the transcripts in 2 groups (scientific and non-scientific).  For each transcript in each group, sentences were generated and fed to the flair `sentiment` Classifier.   This yielded a score between 0 and 1, and a label (POSITIVE or NEGATIVE) for each sentence.  A positive score was kept as is, and a negative score was multiplied by -1 to yield a value between -1 and 0.  These corrected score were averaged per transcript, yielding a date (the date the Youtube video was uploaded) and an average sentiment score.  Repeating this procedure for all transcripts in both groups allowed us to visualize the possible change of sentiment towards AGI in the scientific and non-scientific community. 

## Implementation

All code and data is available in a github repository [@github].  We recap the most important files here : 

- `srt_to_txt.py` contains the code to transform srt subtitle transcripts as downloaded from Youtube to texts without time information or duplicate lines.
- `utils.py` contains several utility methods to load transcripts and their metadata, to iterate over tokens of transcripts, etc.
- `prepare_data.py` contains a script to pre-generate input data used in the jupyter notebooks (e.g. tokenized sentences for all transcripts of a community).
- `wordcloud.ipynb` is a jupyter notebook that performs the wordcloud analysis.
- `ngrams.ipynb` is a jupyter notebook that performs the N-gram analysis.
- `topic.ipynb` is a jupyter notebook that performs the topic modeling analysis.
- `sentiment_analysis.ipynb` is a jupyter notebook that performs the sentiment analysis.

# Evaluation and Results

## RQ 1

In order to evaluate RQ 1, we look at the results of the wordcloud, N-gram and topic modeling analysis.  

Figures @{fig:wordcloud-scientific-before} and @{fig:wordcloud-scientific-after} illustrate the most important words of discussions in the scientific community before and after the introduction of ChatGPT.  A lot of words overlap between these two groups of transcripts.  The transcripts before ChatGPT seem to be mostly positive ("good", "human", "people", "right"), whereas the transcripts after ChatGPT contain more negative words ("problem", "different", "change").

![Wordcloud (scientific community before ChatGPT)](figures/wordcloud-scientific-before.png){#fig:wordcloud-scientific-before height=50% width=50%}

![Wordcloud (scientific community after ChatGPT)](figures/wordcloud-scientific-after.png){#fig:wordcloud-scientific-after height=50% width=50%}


Figures @{fig:wordcloud-non-scientific-before} and @{fig:wordcloud-non-scientific-after} illustrate the most important words of discussions in the non-scientific community before and after the introduction of ChatGPT.  We see the same pattern as in the scientific community.  The discussions after ChatGPT seem to contain more negative words ("problem", "bad", "hard").

![Wordcloud (non-scientific community before ChatGPT)](figures/wordcloud-non-scientific-before.png){#fig:wordcloud-non-scientific-before height=50% width=50%}

![Wordcloud (non-scientific community after ChatGPT)](figures/wordcloud-non-scientific-after.png){#fig:wordcloud-non-scientific-after height=50% width=50%}

We see interesting patterns arise in bigram data for the scientific community, see Figure @{fig:bigrams}.  The conversation seems to have shifted from machine learning and deep learning (before ChatGPT) to large language models (LMM) and super intelligence (after ChatGPT).  We do not see the same shift for the non-scientific community, where the bigrams do not seem to contain any useful information.   Of note however is that "open ai" is one of the top 10 bigrams after the introduction of ChatGPT.

![Bigrams](figures/ngram-bigrams.png){#fig:bigrams}

Trigrams (see Figure @{fig:trigrams}) should be able to capture a bit more context than bigrams.  In the scientific community, we see focus shift from traditional techniques like deep neural nets and self supervised learning (before ChatGPT) to large language models (after ChatGPT).   There seems to be more attention on human level intelligence and AI.  The non-scientific community seems to shift towards a more negative vision after the introduction of ChatGPT, as evidenced by the mention of "brave new world" and "world war iii".

![Trigrams](figures/ngram-trigrams.png){#fig:trigrams}


Figures @{fig:topic-modeling-scientific-before} and @{fig:topic-modeling-scientific-after} illustrate the 6 most important topics determined by an LDA model for the scientific community.  Topic 6 of the scientific community before ChatGPT seems to point in the direction of possible problems with AGI, and topic 3 of the scientific community after ChatGPT seems to be about super intelligence.

Figures @{fig:topic-modeling-non-scientific-before} and @{fig:topic-modeling-non-scientific-after} illustrate the 6 most important topics determined by an LDA model for the non-scientific community.  Here, the focus seems to have shifted from topics about climate change (Topic 4) and (super)human-level intelligence (Topic 6) before ChatGPT to discussions about the replacement of workforce by AGI (Topic 1) and a breakthrough accomplished by the GPT-4 model (Topic 3) after ChatGPT.  

## RQ 2

In order to evaluate RQ 2, we look at the results of a sentiment analysis.  We also look at the general trend over time, to see in which direction the sentiment evolves.  If the slope of the trend line is negative, the sentiment is getting more negative over time.

Figure @{fig:sentiment-scientific} illustrates sentiment evolution over time for the scientific community.  The general trend is negative over time.  Looking at the trend before ChatGPT (Figure @{fig:sentiment-scientific-before}) shows that the slope of the trend line was negative.  Looking at the trend after ChatGPT (Figure @{fig:sentiment-scientific-after}) shows that the slope is decreasing more than before the introduction of ChatGPT.   Slope values are summarized in Table \ref{table:slopes-scientific}.

![Sentiment analysis over time (scientific community)](figures/sentiment-scientific.png){#fig:sentiment-scientific}

| community  | ChatGPT          | slope       |
|------------|------------------|-------------|
| scientific | before and after | -1.5000E-06 |
| scientific | before           | -2.0660E-06 |
| scientific | after            | -3.1671E-06 |

Table: Slope values for scientific community \label{table:slopes-scientific}


Figure @{fig:sentiment-non-scientific} illustrates sentiment evolution over time for the non-scientific community.  Again, the general trend is negative over time.  Looking at the trend before ChatGPT (Figure @{fig:sentiment-non-scientific-before}) shows that the slope of the trend line was negative.  Looking at the the trend after ChatGPT (Figure @{fig:sentiment-non-scientific-after}) shows that the slope is decreasing more than before the introduction of ChatGPT.   Slope values are summarized in Table \ref{table:slopes-non-scientific}.

![Sentiment analysis over time (non-scientific community)](figures/sentiment-non-scientific.png){#fig:sentiment-non-scientific}

| community      | ChatGPT          | slope       |
|----------------|------------------|-------------|
| non-scientific | before and after | -3.3903E-06 |
| non-scientific | before           | -7.0276E-07 |
| non-scientific | after            | -1.0154E-05 |

Table: Slope values for non-scientific community \label{table:slopes-non-scientific}

  
  


# Discussion

To investigate RQ 1, we used wordclouds, bigrams, trigrams and topic modeling techniques to analyze transcripts.   The evaluation of the results of these analyses is mostly subjective : we look at the relevant words, N-grams and topics extracted before and after the introduction of ChatGTP and make a subjective assessment.  We can list some conclusions : 

- there is obviously a lot of overlap in topics discussed before and after the introduction of ChatGPT.
- more words and N-grams having a negative connotation are found in transcripts after the introduction of ChatGPT.  Again, this is a subjective assessment.
- it appears an LDA model was not able to capture many relevant topics given the (very) limited dataset we used

These results do not show clear changes in discussed topics.  As a partial explanation for these results, we can note : 

- wordclouds and N-grams (bigrams in particular) are very simple and limited language models.  There is only so much context you can capture with these models.
- the dataset is small, in particular the non-scientific community corpus (see Table \ref{table:counts}).  Given more input data, an LDA model might have produced more relevant topics.
- the dataset consists of automatically generated transcripts.  The quality of these transcripts might not always be optimal.  

We could carefully conclude for RQ 1 that there is indeed a difference in the topics discussed in the scientific and non-scientific community before and after the introduction of ChatGPT.  Topics discussed after ChatGPT was introduced, appear to be more about problems and risks associated with the use of AGI-like systems like ChatGPT.

The evaluation of RQ 1 was mostly subjective.  For the evaluation of RQ 2, we tried to take a more objective approach by using a sentiment analysis model.  

Results showed discussions remained mostly neutral or slightly positive over time in both communities, with values ranging more or less between 0 and 0.25.  However, we found the general sentiment trendline decreased over time.  We performed the trendline analysis separately for the periods before and after the introduction of ChatGPT, in order to examine whether ChatGPT caused the negative trend in sentiments.  This did not seem to be the case, as sentiment was already becoming more negative before ChatGPT was introduced.  Sentiment decreased faster after the introduction of ChatGPT, allthough the difference in slope values was very minor.  In other words, the general decrease in sentiment is only partly explained by the introduction of ChatGPT.  

We can summarize the evaluation of RQ 2 as follows : in both the scientific and non-scientific community, there is a (small) tendency towards more negative sentiment about AGI after the introduction of ChatGPT.  

Discussing ethical issues about the safe use of generative AI models and ensuring we take the necessary steps to avoid negative consequences as much as possible, is vital if we want to integrate these models in our society.

# Conclusion

In this report, we have analyzed transcripts from Youtube videos about AGI from experts in both the scientific and the non-scientific community.  We wanted to analyze whether the discussions about AGI changed after the introduction of ChatGPT.  We found some subjective change in the topics discussed before and after ChatGPT, going from more positive topics (before ChatGPT) to slightly less positive topics (after ChatGPT).  We also performed a more objective evaluation of the sentiment around AGI by using a sentiment analysis model.  Sentiment appeared to already become less positive in the period leading up to the introduction of ChatGPT, but we found this trend increased slightly after the introduction of ChatGPT.  

The safe use of an AGI system implies it acts ethically and responsibly, and it resists bias.  We did not thoroughly investigate whether ChatGPT can be considered a "real" AGI system. However, assuming we can categorize it as such, we discussed many issues the current ChatGPT models have concerning safety.

We see some opportunities for future work.  Given the small input dataset,  it would be interesting to do a more elobarate analysis using more data.  Second, we limited our analysis to transcripts of Youtube videos.  It makes sense to include other sources as well, like scientific articles, blog articles, etc. 

Whether generative AI model will ultimately benefit society remains to be seen.   We can only applaud the fact that discussions are being held about the ethical risks of these models and how to take the necessary steps to mitigate them.

# References

::: {#refs}
:::

# Appendix A Topic modeling

![Topic modeling (scientific community before ChatGPT)](figures/topic-modeling-scientific-before.png){#fig:topic-modeling-scientific-before}

![Topic modeling (scientific community after ChatGPT)](figures/topic-modeling-scientific-after.png){#fig:topic-modeling-scientific-after}

![Topic modeling (non-scientific community before ChatGPT)](figures/topic-modeling-non-scientific-before.png){#fig:topic-modeling-non-scientific-before}

![Topic modeling (non-scientific community after ChatGPT)](figures/topic-modeling-non-scientific-after.png){#fig:topic-modeling-non-scientific-after}


# Appendix B Sentiment Analysis

![Sentiment analysis before ChatGPT (scientific community)](figures/sentiment-scientific-before.png){#fig:sentiment-scientific-before}

![Sentiment analysis after ChatGPT (scientific community)](figures/sentiment-scientific-after.png){#fig:sentiment-scientific-after}

![Sentiment analysis before ChatGPT (non-scientific community)](figures/sentiment-non-scientific-before.png){#fig:sentiment-non-scientific-before}

![Sentiment analysis after ChatGPT (non-scientific community)](figures/sentiment-non-scientific-after.png){#fig:sentiment-non-scientific-after}
