from trie import Trie

class LongestCommonWord(Trie):
    def __init__(self):
        super().__init__()

    def find_longest_common_word(self, strings) -> str:
        
        """
        Return the longest common prefix of all strings in the list.
        Raises TypeError if input is not a list of strings.
        """

        if not isinstance(strings, list):
            raise TypeError("Input must be a list of strings")
        if not strings:
            return ""
        for s in strings:
            if not isinstance(s, str):
                raise TypeError("All elements must be strings")

        self.__init__()  
        for word in strings:
            self.put(word, True)

        # Walk down the trie while there's exactly one child and not end-of-word
        node = self.root
        prefix_chars = []
        while True:
            children = node.children
            if len(children) != 1 or node.value is not None:
                break
            ch, next_node = next(iter(children.items()))
            prefix_chars.append(ch)
            node = next_node

        return "".join(prefix_chars)


if __name__ == "__main__":
    lcp = LongestCommonWord()

    # Basic tests
    assert lcp.find_longest_common_word(["flower","flow","flight"]) == "fl"
    assert lcp.find_longest_common_word(
        ["interspecies","interstellar","interstate"]
    ) == "inters"
    assert lcp.find_longest_common_word(["dog","racecar","car"]) == ""
    assert lcp.find_longest_common_word([]) == ""

    # TypeError tests
    try:
        lcp.find_longest_common_word(None)
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for non-list input")

    try:
        lcp.find_longest_common_word(["ok", 123])
    except TypeError:
        pass
    else:
        raise AssertionError("Expected TypeError for non-string element")

    print("All tests passed!")
