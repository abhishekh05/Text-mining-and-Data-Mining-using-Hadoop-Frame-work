#!/usr/bin/env python
"""mapper.py"""

import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import sys
nltk.download('stopwords')
nltk.download('punkt')
ps = PorterStemmer() 
sw = set(stopwords.words('english')) 



def concatenate_list_data(list):
    result= ''
    for element in list:
       # print(element)
        result += str(" ")+ str(element)
        #print(result)
    return result


# input comes from STDIN (standard input)
fmap_result = open('Result_Mapper.txt',encoding='utf8')
with open('Articles.txt',encoding="utf8") as f:
    lines = f.readlines()

for line in lines:
    examp=line
    wt = word_tokenize(examp) 
    filtered_sentence = [w for w in wt if not w in sw] 
      
    filtered_sentence = [] 
      
    for w in wt: 
        if w not in sw: 
            filtered_sentence.append(w) 
   # print("first instance of ",filtered_sentence )        
    examp= concatenate_list_data(filtered_sentence)
    #print(examp)
    words = word_tokenize(examp)
    #print(ws)
    filtered_sentence = []
    for w in words: 
        filtered_sentence.append(ps.stem(w)) 
        
    examp= concatenate_list_data(filtered_sentence)
    line= examp
    
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    #print(words)
    # increase counters
    for word in words:
#         write the results to STDOUT (standard output);
#         what we output here will be the input for the
#         Reduce step, i.e. the input for reducer.py
        
       # tab-delimited; the trivial word count is 1
        print ('%s\t%s' % (word, 1))
        fmap_result.write(word)
    