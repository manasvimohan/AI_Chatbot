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

from newspaper import Article
import random, string
import nltk
from sklearn.feature_extraction.text import CountVectorizer

