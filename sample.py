__author__ = 'Abhinav'

import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sentence_tokenizer = PunktSentenceTokenizer(train_text)  #note here that it is a sentence tokenizer

tokenized = custom_sentence_tokenizer.tokenize(sample_text)
#print tokenize

def process():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #print (tagged)
            chunkGram = r"""Chunk : {<RB.?>*<VB.?>*<NNP>+<NN>?} """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print chunked
            chunked.draw()

    except Exception as e:
        print (str(e))

process()