from nltk.sentiment.vader import SentimentIntensityAnalyzer

import json
import logging
import os
import requests

BEARER_TOKEN = ""
RULE = ""
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

def get_rules():
    
    """A function that returns all existing rules."""

    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )

def delete_all_rules():
    
    """A function that deletes all existing rules."""
    
    rules = get_rules()
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )

def set_rules():
    
    """A function that sets a new rule."""
    
    rule = [
        {"value": RULE , "tag": RULE},
    ]
    payload = {"add": rule}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )


def get_stream():
    
    """Prints a stream of polarity scores for all incoming tweets matching current rule."""
    
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
    )
    
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
        
    analyzer = SentimentIntensityAnalyzer()
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            tweet = json_response['data']['text']
            sentiment = analyzer.polarity_scores(tweet)
            print(sentiment)
            


def main():
    delete_all_rules()
    set_rules()
    get_stream()

if __name__ == "__main__":
    main()
