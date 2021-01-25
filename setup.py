import os
import wordnet

log_dir = '/var/log/twitter-sentiment-analysis'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
