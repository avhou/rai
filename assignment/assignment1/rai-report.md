---
title: "IM0802-232434M - Responsible Artificial Intelligence assignment 1"
subtitle: "Deepfakes detection and attribution"
author: "Alexander Van Hecke (852631385)"
institute: "OU"
date: \today
geometry: margin=2.5cm
numbersections: false
link-citations: true
link-bibliography: true
papersize: a4
---

> The aim of this assignment is to write a critical essay on how AI is applied in a specific domain/problem which creates certain consequences for specific stakeholders. In this assignment you will either select one of the topics suggested to you or you will define a topic by yourself. A list with suggested topics is provided to you on yOUlearn in the Assignment 1 section.
> Further, you will search the following resources:
> - two recent scientific articles outside the resources used in the course for the chosen context,
> - one news/blog article that describes the topic selected, and
> - a movie/series/book/etc. that includes relevant aspects to the topic selected.
> The scientific resources are used to capture the scientific perspectives and dimensions of the topic studied, while the non-scientific resources are used to capture the social and cultural perspectives and dimensions of the topic selected and position this topic in the ongoing societal discourses.
> Afterwards, write a small paragraph describing the topic selected and resources you plan to use and send them to the teacher for verification. In case of unclarities, this process can repeat until it is clear. In case the topic and approach are clear, the student can send a document of max. one page with the outline of this assignment for verification and feedback from the teacher.
> Write a critical essay of around 2500 words (exclusive references) on how the AI method/application produces certain consequences in the context selected to certain stakeholders following the requirements presented below.

movies : 
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10325052/#:~:text=There%20are%20growing%20concerns%20about,versions%20of%20the%20same%20actor.
For example, in the Star Wars TV show “The Book of Boba Fett”, the character of Luke Skywalker is played by an actor with a younger version of the original Luke Skywalker (actor Mark Hamill) superimposed onto their face [15]
King J. Deepfake Luke Skywalker is another step down a ghoulish CGI path. GQ. 2022 February 10. Available from: https://www.gq-magazine.co.uk/culture/article/boba-fett-luke-skywalker.

# Introduction

> introduce the aim and motivation of the essay considering the following setting:
> Introduce the aim of the essay using a small ethical dilemma/scenario as a fictional setting that illustrates the context. You can consider this an instantiation of consequences created by applying AI in a certain domain or problem.
> The purpose of this ethical dilemma/scenario is to capture the interest and attention of the reader and state the need to tackle this topic. For this include the following scenario elements: setting, action, and impact.
> On this behalf, you can use the article by Wright et al. (2014) describing ethical dilemma scenarios available here:
> Wright, D., Finn, R., Gellert, R., Gutwirth, S., Schütz, P., Friedewald, M., ... & Mordini, E. (2014). Ethical dilemma scenarios and emerging technologies. Technological Forecasting and Social Change, 87, 325-336.

In this essay we want to describe a dark scenario ``Surely this is something I can trust?''.  In this scenario we discuss Peter, a young man that is just starting to get settled, is in a stable financial situation and has a couple of years of working experience.  Peter tries to stay informed about current events and uses diverse sources of information for this.  He watches the news on national television regularly, but also checks several social media feeds to see what's happening in the world.  The social media companies decide what Peter gets to see on his feed, and they try to maximize the screen time of Peter, as more screen time means more advertisements can be shown to Peter.  Trying to maximize screen time and selling ads is the business model of the social media companies, and they distribute all kinds of media (text, short stories, videos, etc) to maximize their profits.

One day, Peter gets a video on his feed where a well known financial journalist Michael praises an investment.  As Peter has been doing well financially lately, he has some financial reserves and he has already been thinking about investing his money in some way.  However, since he is no financial expert, he didn't know how to get started.  This seems like an excellent opportunity to Peter, since he knows Michael from national television where he often discusses economy and financial topics on the news.  Peter fully trusts Michael, as he always has a nuanced opinion and generally seems very knowlegdeable about investments.  After looking at the website of the investment, he decides it looks good and invest all his money in this opportunity.

Unfortunately, the video was a deepfake video.  Scammer Kris created this video using freely available software, and was able to use a lot of video and speech from Michael's television appearances.  Bert was abusing Michael's good name and financial reputation to lure people in a fake investment.  Needless to say, all money invested goes straight to Kris.  Michael was not aware of this video, and certainly does not endorse the investment praised in the deepfake video.

This scenario is happening today.  Two very recent cases in Belgium illustrate this.  A deepfake video of financial journalist Michael Van Droogenbroeck was distributed on social media [@vrt1], and news anchor Annelies Van Herck appeared in a deepfake video where she advertises a ``get rich quick'' game [@vrt2].  These videos were widely distributed on social media, and lots of people fell for these scams.  Social media companies are aware of this issue [@meta;@google] but don't do enough to prevent this from happening as it goes against their business model.  Meanwhile, scammers are getting away with this and trick people in their fake investments.

# Issue

> summarize the content of the four resources used and define the issue discussing the following elements:
> • Discuss how and where AI is applied to tackle the chosen problem/domain.
> • Discuss why and how consequences of AI application are created reflecting on who are the stakeholders experiencing/impacted by these consequences.
> • Explain why applying AI in this setting can be considered an issue or a challenge from an ethical perspective and argue if this represents a new or an old (well-known) problem in this domain. At the same time, reflect if this issue appears only due to the application of AI or also other (societal) factors are involved or take part in this process.

Deepfake videos are pervasive in the media.  Recently, hyper-realistic videos have emerged that depict someone say and do things that never happened.  Given the reach and speed of social media, convincing deepfakes can quickly reach millions of people and have negative impacts on our society [@scholar1].  Academic research has focused not only on generative models and generative adverserial networks (GANs) capable of generating deepfake videos, but also on ways to detect deepfake videos by these architectures.  A convolutional neural network (CNN) with a classifier network is proposed by the authors of [@scholar2] for the detection of deepfake videos.  They extract faces from videos and compare these against a face dataset [@facedataset] to detect deepfake videos.  Their technique works especially well on videos generated by an autoencoder.  The use of transfer learning is examined in [@scholar3].  Transfer learning in autoencoders and a combination of CNN and Recurrent Neural Network (RNN) models are used to increase detection rates of deepfake videos when these are generated using unseen manipulations and datasets.  They conclude fine-tuned yield better accuracy as compared to models trained from scratch.

Several news anchors of VRT.nws, a public news outlet in Belgium 

stakeholders : 
- scammers: financial gain
- victims, both those who fall for the scam and those whose identities are abused
- companies the people whose identities are abused work for (i.e. VRT)
- social media companies
- to a lesser extent : people selling / making deepfake video software.  These people do not necesarilly have bad intentions.   cfr wright people feel only partially responsible.  unforeseeable consequences

issues : 
- privacy : financial data (i.e. credit card data) is stolen
- ethical : this is theft and abuse of trust

# Solution

> consider as a starting point (i) either existing solutions to tackle the identified issue and propose ways to enhance them or (ii) propose your own solution(s) to tackle the identified issue. In both cases, include the following aspects and relate them to the influence on impacted stakeholders:
> • Ethics: discuss ethical aspects and frameworks involved in building and applying the existing/proposed solution(s).
> On this behalf, you can use the article by Mittelstadt et al. (2016) describing debates on ethical aspects surrounding the application of AI algorithms, available here:
> Mittelstadt, B. D., Allo, P., Taddeo, M., Wachter, S., & Floridi, L. (2016). The ethics of algorithms: Mapping the debate. Big Data & Society, 3(2), 2053951716679679.
> Note that you can use this recommended article, or another article found by you, to discuss the ethical aspects. Do not forget to mention it in the references of the assignment.
> • Regulation: discuss how this issue could be regulated or how is already regulated considering existing applied regulation frameworks.
> • Society: discuss the societal perception and mechanisms of tackling this issue. You can think here of mechanisms such as governmental programs, NGO initiatives, dedicated standards (e.g., IEEE and ISO) etc.
> • Personal reflection: provide your own perspective on the identified issue and existing/found solutions to tackle it.

# Conclusions

> provide concluding remarks for the issue identified and existing/applied solution using the four resources found by yourself and relate these findings to your personal assessment following the structure below:
> • Discuss one or two concluding remarks.
> • Discuss the findings on the existing/proposed solution
> considered to tackle the issue identified.
> • Provide an answer and own reflection to the following question: In your opinion, is the existing/proposed solution suitable to tackle the identified issue or should it be considered a total change in approaching it?

# References

::: {#refs}
:::
