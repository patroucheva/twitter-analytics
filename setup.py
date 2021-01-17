import os

log_dir = '/var/log/twitter-sentiment-analysis'

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

