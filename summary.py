'''
-----------------------------------------------------------------------
Created by Manasvi Mohan Sharma on 09/01/21 (mm/dd/yy)
Project Name: AI_Chatbot | File Name: summary.py
IDE: PyCharm | Python Version: 3.8
-----------------------------------------------------------------------
                                       _ 
                                      (_)
 _ __ ___   __ _ _ __   __ _ _____   ___ 
| '_ ` _ \ / _` | '_ \ / _` / __\ \ / / |
| | | | | | (_| | | | | (_| \__ \\ V /| |
|_| |_| |_|\__,_|_| |_|\__,_|___/ \_/ |_|

GitHub:   https://github.com/manasvimohan
Linkedin: https://www.linkedin.com/in/manasvi-mohan-sharma-119375168/
Website:  https://www.manasvi.co.in/
-----------------------------------------------------------------------
Project Information:
Part of AI Chatbot

About this file:
This file is summary script, which makes summary out of large text.
-----------------------------------------------------------------------
'''

import random
import wikipedia
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import download

download('wordnet', quiet=True)

def _create_frequency_table(text_string) -> dict:

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    wnl = WordNetLemmatizer()

    freqTable = dict()
    for word in words:
        word = wnl.lemmatize(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable

def _score_sentences(sentences, freqTable) -> dict:
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[:10] in sentenceValue:
                    sentenceValue[sentence[:10]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[:10]] = freqTable[wordValue]

        sentenceValue[sentence[:10]] = sentenceValue[sentence[:10]] // word_count_in_sentence

    return sentenceValue

def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return average

def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[:10] in sentenceValue and sentenceValue[sentence[:10]] > (threshold):
            summary += "\n*" + sentence
            sentence_count += 1

    return summary

print('What do you wish to know about?')
topic = input('Input Here : ')
topic_list = wikipedia.search(topic)
topic = random.choice(topic_list)
print("\nLet's find something about '{}'.".format(topic))

all_info = wikipedia.page(topic)
text = all_info.content

# 1 Create the word frequency table
freq_table = _create_frequency_table(text)
# 2 Tokenize the sentences
sentences = sent_tokenize(text)
# 3 Important Algorithm: score the sentences
sentence_scores = _score_sentences(sentences, freq_table)
# 4 Find the threshold
threshold = _find_average_score(sentence_scores)
# 5 Important Algorithm: Generate the summary
summary = _generate_summary(sentences, sentence_scores, 1.3 * threshold)

print(summary)

