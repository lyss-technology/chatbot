# Created by : Prem Ranjan Pattanayak
# Github Account : premptk
# This chatbot is based on cosine similiarity. It takes data input from a URL using Article package and finds out the most relatable line(answer) with respect to the query asked by user.

from newspaper import Article
import random
import nltk
import string

# used to transform a given text into a vector basis of the frequency of each word that occurs in the entire text
from sklearn.feature_extraction.text import CountVectorizer

# returns score after comparing answer with input text
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import warnings

warnings.filterwarnings('ignore')

# nltk tokenizer requires punkt package
nltk.download('punkt', quiet=True)

# get the article
article = Article('https://en.wikipedia.org/wiki/Coronavirus')
article.download()
# removes html, links and extra unnecessary things
article.parse()
article.nlp()
corpus = article.text
# print(corpus)

# Tokenization
test = corpus
sentence_list = nltk.sent_tokenize(test)  # returns a list of sentences derived from paragraph


# print(sentence_list)


# A function to return greeting to user
def greet_res(text):
    text = text.lower()
    bot_greetings = ['Hi', 'Hello', 'hey', 'wassup']
    user_greetings = ['hii', 'hello', 'helo', 'hey', 'hi']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)


# Fuction for the index
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                # swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
    return list_index


# Function for bot response
def bot_resp(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_res = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    s_score = cosine_similarity(cm[-1], cm)
    s_score_list = s_score.flatten()
    # print(s_score_list)
    index = index_sort(s_score_list)
    index = index[1:]
    resp_flag = 0

    j = 0
    for i in range(len(index)):
        if s_score_list[index[i]] > 0.0:
            bot_res = bot_res + ' ' + sentence_list[index[i]]
            resp_flag = 1
            j = j + 1
        if j > 2:  # number of response lines
            break

    if resp_flag == 0:
        bot_res = 'I am sorry, I could not understand your query. Please be more specific!'

    sentence_list.remove(user_input)

    return bot_res


# Start the chat
print('     Covid Helpline \nI am here to help you regarding Corona Virus\n Enter quit/exit to exit the chat')

exit_list = ['quit', 'exit', 'bye', 'byee']

while True:
    user_input = input()
    if user_input.lower() in exit_list:
        print('Bot: Thanks for your queries!\n Please visit again!')
        break
    else:
        if greet_res(user_input) is not None:
            print('Bot: ' + greet_res(user_input))

        else:
            print('Bot: ' + bot_resp(user_input))
