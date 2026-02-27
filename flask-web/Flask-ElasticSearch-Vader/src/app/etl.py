#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pandas as pd
from google_trans_new import google_translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class TransformData():
    def __init__(self, data, messages):
        self.data = data
        self.messages = messages

    def get_sentiments(self):
        df = self.data
        translator = google_translator()
        analyzer = SentimentIntensityAnalyzer()

        for i, row in df.iterrows():
            translate = translator.translate(row[self.messages], lang_tgt='en')
            df.at[i, 'translate'] = translate

        for i, row in df.iterrows():
            vs = analyzer.polarity_scores(row['translate'])
            df.at[i, 'neg'] = vs['neg']
            df.at[i, 'neu'] = vs['neu']
            df.at[i, 'pos'] = vs['pos']
            df.at[i, 'compound'] = vs['compound']
        
        return df