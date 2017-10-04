
def is_anagram(a_word, b_word):
    """
    >>> is_anagram("abc", "acb")
    True
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("one", "two")
    False
    """
    return sorted(a_word) == sorted(b_word)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

