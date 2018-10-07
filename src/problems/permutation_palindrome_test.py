from unittest import TestCase
from .permutation_palindrome import is_any_permutation_palindrome


class PermutationPalindromeTest(TestCase):
    def test_perm_palindrome(self):
        true_words = ["civic", "ivicc"]
        false_words = ["civil", "livci"]

        for word in true_words:
            with self.subTest(word=word):
                self.assertTrue(is_any_permutation_palindrome(word))

        for word in false_words:
            with self.subTest(word=word):
                self.assertFalse(is_any_permutation_palindrome(word))
