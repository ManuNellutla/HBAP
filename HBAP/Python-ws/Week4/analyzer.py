
import os
import sys


class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self):
        """Initialize Analyzer."""

        # instantiate tokenizer
        #self.tokenizer = nltk.tokenize.TweetTokenizer()

        # load positive words
        self.positives = set()
        self.negatives = set()

        self.positives.add("good")
        self.negatives.add("bad")

    def analyze(self, text):
        """Analyze text for sentiment, returning a score."""

        # tokenize text
        tokens = text.split(" ")

        # score text
        score = 0
        for token in tokens:
            token = token.lower()
            if token in self.positives:
                score += 1
            if token in self.negatives:
                score -= 1
        return score