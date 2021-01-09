'''
-----------------------------------------------------------------------
Created by Manasvi Mohan Sharma on 09/01/21 (mm/dd/yy)
Project Name: AI_Chatbot | File Name: experiment_file.py
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
About this file:
-----------------------------------------------------------------------
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def cos_sim(X,Y):
    # Word Tokenization
    X_list = word_tokenize(X)
    Y_list = word_tokenize(Y)

    # Create list of stopwords
    sw = stopwords.words('english')
    l1 = []
    l2 = []

    # Remove stop words from the strings
    X_set = {w for w in X_list if not w in sw}
    Y_set = {w for w in Y_list if not w in sw}

    # form a set containing keywords of both strings
    rvector = X_set.union(Y_set)
    for w in rvector:
        if w in X_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in Y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0

    # cosine formula
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    print("similarity: ", cosine)
    return cosine

X = "I love horror movies"
Y = "Lights out is a horror movie"
cosine = cos_sim(X,Y)