"""
Empty Compose Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

#1 get words from text
#2 create a graph using those words
#3 get the next word for x number of words
#4 show the user

import os
import re
import string
import random

from graph_template import Graph, Vertex

def get_words_from_text(text_path):
    with open(text_path,'r') as f:
        text = f.read()
        text = ' '.join(text.split()) # this is saying turn whitespace in just spaces
        text = text.lower()
        text = text.translate(str.maketrans('','', string.punctuation)) #removes punctuation

    return text.split()
def make_graph(words):
    g = Graph()
    # for each word in words
    previous_word = None
    for word in words:
    #check if that word is in the graph, and if not then add it
    # if there was a previous word, then add and edge if it does not already exist
        word_vertex = g.get_vertex(word)#checks if vertex exists, if not then creates one(dictionary entry and instance of class Vertex)
        if previous_word:
            previous_word.increment_edge(word_vertex)

    # in the graph, otherwise increment freuency by 1
    # set our word to the previous word and iterate!
        previous_word = word_vertex


    #now remember that we want to generate the probability mappings before composing
    #this is a great place to do it before we return the graph object
    g.generate_probability_mappings()

    return g



def compose(g, words, length=50): #a graph, our words and a lenght of composition
    composition = []
    word = g.get_vertex(random.choice(words))
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)
    return composition

def main():
    #1 get words from text
    words = get_words_from_text('texts/hp_sorcerer_stone.txt')
    #2 create a graph using those words
    g = make_graph(words)
    #3 get the next word for x number of words as defined by the user

    #4 show the user
    composition = compose(g, words, 100)
    return ' '.join(composition) # returns a string, where all the words are separated by a space!!


if __name__ == '__main__':
    print(main())
