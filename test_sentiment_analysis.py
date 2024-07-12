from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def text_sentiment_analyzer(self):
        testcase_one = sentiment_analyzer('I love working with Python')
        self.assertEqual(testcase_one['label'],'SENT_POSITIVE')
        testcase_two = sentiment_analyzer('I hate working with Python')
        self.assertEqual(testcase_two['label'], 'SENT_NEGATIVE')
        testcase_three = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(testcase_three['label'], 'SENT_NEUTRAL')

unittest.main()