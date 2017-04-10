# put your code here.
 # create empty dictionary
 # open text file
 # for loop that iterates over text file and adds to dictionary with counts
 # somewhere print it out the dictionary both keys and values

import string

def get_word_count(text_file):

    word_count = {}
    exclude = []
    exclude = set(string.punctuation)
    exclude = exclude - {"-", "'", "."}

    for line in text_file:
        line = line.rstrip()
        word_list = line.split(" ")

        for word in word_list:
            word = word.lower()
            word = ''.join(ch for ch in word if ch not in exclude)
            word = word.rstrip(".")
            word = word.lstrip("'")
            word_count[word] = word_count.get(word, 0) + 1

    # print word_count
    return word_count

def print_word_count(word_count):

    for word, count in word_count.items():
        print "%s: %d" % (word, count)


file_text = open("twain.txt")
# get_word_count(file_text)
print_word_count(get_word_count(file_text))

# open file outside of function