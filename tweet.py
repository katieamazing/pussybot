#!/usr/bin/env python3

import imgs

import os, sys, codecs, yaml, random, requests
import nltk.data
from bs4 import BeautifulSoup
from io import BytesIO
from twython import Twython


def generate_tweet_text():
    sys.stdout = codecs.getwriter("utf8")(sys.stdout)
    sys.stderr = codecs.getwriter("utf8")(sys.stderr)

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
    return random.choice(possible).replace("  ", " ")

tweet_image = random.choice(imgs.imgs)
print(tweet_image)
tweet_text = generate_tweet_text()
print(tweet_text)


with open("C:\PussyBot\config.yaml") as f:
    config = yaml.load(f)

twitter_app_key = config["twitter_app_key"]
twitter_app_secret = config["twitter_app_secret"]
twitter_oauth_token = config["twitter_oauth_token"]
twitter_oauth_token_secret = config["twitter_oauth_token_secret"]

twitter = Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)

res = requests.get(tweet_image)
image_io = BytesIO(res.content)


# Twitter upload, tweet

image_io.seek(0)

response = twitter.upload_media(media=image_io)
twitter.update_status(status=tweet_text, media_ids=[response['media_id']])
