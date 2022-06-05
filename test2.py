#
# test using original dictionary
# # importing the nltk suite
import nltk
import re
from wrong import wrongw
from correct import corrected_words
# importing jaccard distance
# and ngrams from nltk.util
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
# Downloading and importing
# package 'words' from nltk corpus
nltk.download('words')
from nltk.corpus import words
def process_text(path):
    words1 = []
    with open(path) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words1 = re.findall(r'\w+',file_name_data)

    return words1

book_words = process_text('kidsbook.txt')

correct_words = words.words()
# list of incorrect spellings
# that need to be corrected

count=0
for x in wrongw:
    incorrect_words=x

    temp = [(jaccard_distance(set(ngrams(incorrect_words, 2)),
                    set(ngrams(w, 2))),w)
	    for w in book_words if w[0]==incorrect_words[0]]	  
    output = sorted(temp, key = lambda val:val[0])[0][1]
    if output in corrected_words:
        count+=1

print(count," out of 100")