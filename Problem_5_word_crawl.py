# Word Crawler
#   By Samuel Leonard
#
#   This script will crawl through a text and count the number of times each word shows up.
#
#
#
import operator
text_path = "E:\\A_Masters_Program\\501\\Lab_3\\HP_Lovecraft.txt"
Cthulhu_text = open(text_path) 
main_list = Cthulhu_text.read()
clean_word = []

# This function cleans the text and removes any charecters or punctuation, and appends a new list
def clean_up():
    word_trial = main_list.lower().split()
    clean_word_list = []
    for new_word in word_trial:
        symbols = "!@#$%^&*()_+{}[]|:<>?/\",.;'[]\=-"
        for i in range(0, len(symbols)):
            new_word = new_word.replace(symbols[i], "")
        if len(new_word) > 0:
            clean_word_list.append(new_word)
    create_dictionary(clean_word_list)
# This function then performs the word sort and count.
def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
     #sort this dictionary by (0 for key, 1 for values)
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
       print (key, value)

print ("uncle", value)
    
clean_up()

# Much of this code was obtained from https://buckysroom.org/forum/topic.php?id=1982 
