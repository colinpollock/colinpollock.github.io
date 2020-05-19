---
Title: sonorant.io
Date: 2020-03-06
Category:
Tags: linguistics, language models, pytorch,
Description: sonorant.io is a web app that lets you iteratively build novel English words by choosing a phoneme (i.e. sound) from a language model's predictions of the next phoneme, one at a time.
Slug: sonorant-io
---

[sonorant.io][1] is a web app that lets you iteratively build novel English words by choosing a phoneme (i.e. sound) from a language model's predictions of the next phoneme, one at a time.

![Hello!](/images/sonorant-hello.png "Hello!")

## Background

Spelling in English is often ambiguous and misleading, so linguists use the [International Phonetic Alphabet], or IPA, to phonetically represent words. The [CMU Pronouncing Dictionary][3] contains pronunciations in IPA[^1] for about 125 thousand words. As an example, the CMU Dict entry for “catfish” is __/ˈkætˌfɪʃ/__.

I [trained a language model][4] over these pronunciations and used it to power the UI screenshotted above. Most language models you'll find on the web are modeling how likely full sentences are, but this one models how likely a sequences of sounds is to be an English word.

Any language model can be used to generate novel sequences of tokens by repeatedly calculating the distribution for what should come next, sampling from the distribution, adding that sampled token to the word, and repeating. It’s common to automate this whole process and have the computer program do the sampling, but for the app I made it’s up to the human to do the sampling.

## The App
When you first see the app you haven’t chosen any phonemes yet so your word is empty and looks like this: __//__. The chart is a distribution over all phonemes representing which ones the model believes are most likely to come at the beginning of the word. If you click on any phoneme then your word will be updated and the chart will update to represent the distribution for the following phoneme. The updated pronunciation will also be played as audio. You can continue clicking until you click the __<END\>__ token, which finishes your word.

## Playing with the Model
The model has learned that the phoneme __/s/__ is very likely at the beginning of a word but that __/ŋ/__ is extremely unlikely. It has also learned that /ˈstr/ is a valid beginning to a word but __/ˈstm/__ is not.

Here are a few things you can try to do:

* Make the longest word you can.
* Make a word that isn’t actually pronouncable.
* Always select the most likely phoneme to see what the model thinks is the most likely English word. You can also do this after giving a starting point, which would e.g. show you that the most likely word starting with __/ˌtʃ/__ is __/ˌtʃɑːnˈstɛntən/__.


[1]: http://sonorant.io
[2]: https://en.wikipedia.org/wiki/International_Phonetic_Alphabet
[3]: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
[4]: https://github.com/colinpollock/sonorant/blob/master/Model%20Training.ipynb
[5]: https://en.wikipedia.org/wiki/ARPABET
[6]: https://github.com/menelik3/cmudict-ipa

[^1]: The CMU Dictionary was originally in [ARPABET][5], but I used [this version][6] converted to IPA.
