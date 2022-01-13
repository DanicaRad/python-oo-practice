"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """A class used to represent a dictionary (like Webster, not Python) from a text file with one word per line.

    >>> wf = WordFinder('new.txt')
    3 words read

    >>> wf._random(0)
    'cat'

    >>> wf._random(2)
    'porcupine'

    >>> wf._random(1)
    'dog'

    >>> wf2 = WordFinder('words.txt')
    235886 words read

    >>> wf2._random(7)
    'aardvark'

    >>> wf2._random(4264)
    'Ah'

    >>> wf2._random(25737)
    'branchial'

    >>> wf2._random(107236)
    'liquorishness'

    >>> wf2._random(235777)
    'zygomatic'

    """

    def __init__(self, file):
        "Creates a dictionary of words from file path"
        self.file = file
        self.words = self.get_words()
        self.length = len(self.words)

    def __repr__(self):
        return f"WordFinder(file='{self.file}', words=[{self.words[0]}...  {self.words[-1]} total_words={self.length}"

    def get_words(self):
        "Reads and creates a list of words from file"
        read_file = open(self.file, 'r')

        words = [line.strip() for line in read_file]

        print(f"{len(words)} words read")

        read_file.close()

        return words

    def random(self):
        "Prints a random word from the dictionary"
        rand_idx = randint(0, self.length - 1)
        
        return self.words[rand_idx]

    def _random(self, num):
        "Tests random function with hardcoded number"
        return self.words[num]


class SpecialWordFinder(WordFinder):
    """Creates a dictionary from words in file, ignoring whitespace and comments

    >>> wf = SpecialWordFinder('messy.txt')
    4 words read

    >>> wf._random(0)
    'kale'

    >>> wf._random(1)
    'parsnips'

    >>> wf._random(2)
    'apple'

    >>> wf._random(3)
    'mango'

    >>> wf2 = SpecialWordFinder('words.txt')
    235886 words read

    >>> wf2._random(7)
    'aardvark'

    >>> wf2._random(4264)
    'Ah'

    >>> wf2._random(25737)
    'branchial'

    >>> wf2._random(107236)
    'liquorishness'

    >>> wf2._random(235777)
    'zygomatic'
    
    """

    def __init__(self, file):
        "Creates dictionary of list of words from file path"
        super().__init__(file)

    def get_words(self):
        "Creates list of words, ignoring white space and comments"

        read_file = open(self.file, 'r')
        invalid = ("#", "\n")

        words = [line.strip() for line in read_file if not line.startswith(invalid) and len(line) > 1]

        print(f"{len(words)} words read")

        read_file.close()

        return words

