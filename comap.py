#!/usr/bin/env python
"""mapper.py"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import sys
import re




nltk.download('stopwords')
nltk.download('punkt')
ps = PorterStemmer()
sw = set(stopwords.words('english'))



def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(" ")+ str(element)
    return result


# input comes from STDIN (standard input)


for line in sys.stdin:
    #print(line )
    
    
    #line = re.sub('[^a-zA-Z]+', '', line)
    examp=line
    #print(examp)
    wt = word_tokenize(examp)
    filtered_sentence = [w for w in wt if not w in sw]
    
    filtered_sentence = []
    
    for w in wt:
        if w not in sw:
            filtered_sentence.append(w)

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
    # increase counters
common=[
'would'   ,
'amp'  ,
'illeg'   ,
'immigr'  ,
'realdonaldtrump' ,
'wall'    ,
'trump'   ,
'border'  ,
'borderwal'   ,
'http'    ,
'suffer'  ,
'lost'    ,
'someth'  ,
'pleas'   ,
'life'    ,
'trump'   ,
'immigr'  ,
'backfiretrump'   ,
'potu'    ,
'http'   , 

# Twitter top 10
'immigrationpolici',   
'citi'    ,
'democrat'  ,  
'like'    ,
'law' ,
'work' ,   
'new' ,
'need' ,   
'border',  
'amp' ,
'trump',   
'http'  ,  
'cher'    ,
'democrat'    ,
'like'    ,
'polici'  ,
'law' ,
'peopl'   ,
'work'    ,
'new' ,
'daca'    ,
'immigrationcrisi'    ,

'immigrationpolici',   
'need'    ,
'border'  ,
'citi'    ,
'illeg'   ,
'amp' ,
'realdonaldtrump' ,
'trump'   ,
'immigr'  ,
'http'    ,
# Ny data top 10
        'american',
        'one',
        'polici',
        'time',
        'like',
        'peopl',
        'unit',
        'govern',
        'year',
        'new',
        'would',
        'presid',
        'state',
        'democrat',
        'border',
        'trump',
        'immigr',
        'said',
        'best'    ,
'foo' ,
'life'    ,
'lift'    ,
'live'    ,
'planet' ]

cone= ['mexico', 'border', 'pay']
    
print(words)

for i in range(0,len(words)-1):

    if((words[i] in common)):
        for j in range(i+1, len(words)):
             if((words[j] in common)):
                print ('%s-%s\t%s' % (words[i],words[j], 1))


# write the results to STDOUT (standard output);
# what we output here will be the input for the
# Reduce step, i.e. the input for reducer.py
#
# tab-delimited; the trivial word count is 1


