#!/usr/bin/env python3

import imgs
from bs4 import BeautifulSoup
import os, sys, codecs, random
import nltk.data
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

with open("C:\PussyBot\PUSSY AND HER LANGUAGE (Marvin R. Clark, 1895).html") as f:
    body = f.read()
soup = BeautifulSoup(body, "lxml")
text = soup.get_text()

tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
sentences = nltk.sent_tokenize(text)
possible = []
keywords = ("cat", "pussy", "kitten", "meow", "milk", "mouse", "play", "purr", "fish", "eyes", "sleep", "eat", "animal", "feline", "claw")
for s in sentences:
    if len(s) > 50 and len(s) < 140 and any(keyword in s.lower() for keyword in keywords):
        possible.append(s)

tweet_image = random.choice(imgs.imgs)
print(tweet_image)

tweet_text = random.choice(possible)


print(tweet_text)
