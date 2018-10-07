from unittest import TestCase
from .word_cloud import calc_word_cloud
import collections


class WordCloudTest(TestCase):
    def test_word_cloud(self):
        line = "After beating the eggs, Dana read the next step:"
        c = collections.Counter()
        c["after"] += 1
        c["beating"] += 1
        c["the"] += 2
        c["eggs"] += 1
        c["dana"] += 1
        c["read"] += 1
        c["next"] += 1
        c["step"] += 1
        a = calc_word_cloud(line)
        self.assertEqual(a, c)
