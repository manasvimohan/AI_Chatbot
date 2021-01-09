'''
-----------------------------------------------------------------------
Created by Manasvi Mohan Sharma on 09/01/21 (mm/dd/yy)
Project Name: AI_Chatbot | File Name: main.py
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
This project aims to create a simple AI driven chatbot for
demonstration purpose

About this file:
This is the main file.
-----------------------------------------------------------------------
'''

import wikipedia
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

from nltk import download
from nltk.tokenize import sent_tokenize

download('punkt', quiet=True)

def get_summary(topic):
    # corpus = wikipedia.summary(topic, 100)
    # text = corpus
    corpus = wikipedia.page(topic)
    text = corpus.content
    sentence_list = sent_tokenize(text)
    return sentence_list

def response_greeting(text):
    text = text.lower()
    bot_greetings = ['hi','hello','hey']
    user_greetings = ['hi', 'yo','howdy','hello','whats up']
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0,length))
    x=list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index

def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1],cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index =index[1:]
    response_flag = 0
    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response +' '+ sentence_list[index[i]]
            response_flag = 1
            j+=1
        if j>2:
            break
    if response_flag == 0:
        bot_response = bot_response + ' ' + 'Sorry, did not understand'
    return bot_response

print('Bot: Hi, please tell me your topic of interest.')
topic = input()

print(wikipedia.search(topic))
sentence_list = get_summary(topic)
print('I am ready, ask me anything')

exit_list = ['bye','exit','later']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print('Bot: See Ya')
        break
    else:
        if response_greeting(user_input) != None:
            print('Bot: ' + response_greeting(user_input))
        else:
            print('Bot: ' + bot_response(user_input))