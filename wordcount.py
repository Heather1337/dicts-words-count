import string 

def count_words(file):
    """
    Returns the count of all words in provided file argument. 

    Input is a text file.
    Output prints words and count to the terminal.

    Return:
        >>> count_words("test.txt")
        As 1
        I 2
        was 1
        going 2
        to 2
        St. 2
        Ives 1
        met 1
        a 1
        man 1
        with 1
        seven 4
        wives 1
        Every 3
        wife 1
        had 3
        sacks 1
        sack 1
        cats 1
        cat 1
        kits 1
        Kits, 1
        cats, 1
        sacks, 1
        wives. 1
        How 1
        many 1
        were 1
        Ives? 1
    """
    punc = ",.?"

    count_words = {}
    open_file = open(file)
    for line in open_file:
        split_line = line.rstrip().lower().split(' ')
        print(split_line)
        for word in split_line:
            stripped_word = word.rstrip(",.?")
            count_words[stripped_word] = count_words.get(stripped_word, 0) + 1

    for word, count in count_words.items():
        print(word, count)

count_words("test.txt")

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()