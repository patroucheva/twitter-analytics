# twitter-analytics

twitter-analytics is a Python tool for streaming polarity scores of tweets for a custom rule.

## Installing Prerequisites

From within the repository run:

```bash
pip3 install -r requirements.txt
python3 setup.py
```

## Usage

[BEARER_TOKEN](https://developer.twitter.com/en/docs/authentication/oauth-2-0) and [RULE](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/build-a-rule) need to be set in /twitter_sentiment_analysis/scrape.py.

From within the repository run:

```python
python3 twitter_sentiment_analysis
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
