from trie import Trie

class Homework(Trie):
    def __init__(self):
        super().__init__()

    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Count how many words in the trie end with the given suffix `pattern`.
        Raises TypeError if pattern is not a string.
        """
        if not isinstance(pattern, str):
            raise TypeError("suffix pattern must be a string")
        count = 0
        for word in self.keys():
            if word.endswith(pattern):
                count += 1
        return count

    def has_prefix(self, prefix: str) -> bool:
        """
        Return True if there is at least one word in the trie
        that starts with `prefix`. Raises TypeError otherwise.
        """
        if not isinstance(prefix, str):
            raise TypeError("prefix must be a string")
        return bool(self.keys_with_prefix(prefix))


if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, w in enumerate(words):
        trie.put(w, i)

    # count_words_with_suffix
    assert trie.count_words_with_suffix("e")   == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a")   == 1  # banana
    assert trie.count_words_with_suffix("at")  == 1  # cat

    # has_prefix
    assert trie.has_prefix("app")  is True   # "apple", "application"
    assert trie.has_prefix("bat")  is False  
    assert trie.has_prefix("ban")  is True   # "banana"
    assert trie.has_prefix("ca")   is True   # "cat"

    print("All tests passed!")  
