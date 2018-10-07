from unittest import TestCase
from .word_cloud import calc_word_cloud_n
import collections


class WordCloudTest(TestCase):
    def setUp(self):
        self.line = "After beating the eggs, Dana read the next step:"
        self.c = collections.Counter()
        self.c["after"] += 1
        self.c["beating"] += 1
        self.c["the"] += 2
        self.c["eggs"] += 1
        self.c["dana"] += 1
        self.c["read"] += 1
        self.c["next"] += 1
        self.c["step"] += 1

        self.line2 = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
        self.c2 = collections.Counter()
        self.c2["we"] = 4
        self.c2["came"] = 1
        self.c2["saw"] = 1
        self.c2["conquered"] = 1
        self.c2["then"] = 1
        self.c2["ate"] = 1
        self.c2["bills"] = 1
        self.c2["mille"] = 1
        self.c2["feuille"] = 1
        self.c2["cake"] = 1

    def test_word_cloud_n(self):
        a = calc_word_cloud_n(self.line)
        self.assertEqual(a, self.c)
        b = calc_word_cloud_n(self.line2)
        print(b)
        print(self.c2)
        self.assertEqual(b, self.c2)
