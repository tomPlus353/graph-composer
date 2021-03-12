
"""
Empty Graph Template to implement :D

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adjacent = {} # keep track of nodes that have an edge from this vertex
        self.neighbors = []
        self.neighbors_frequency = []
        pass

    def add_edge_to(self, vertex, frequency=0):
        self.adjacent[vertex] = frequency

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) +  1

    def get_adjacent_nodes(self):
        self.adjacent

    # initializes probability map
    def get_probability_map(self):
        for (vertex, frequency) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_frequency.append(frequency)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_frequency)[0] 



class Graph(object):
    def __init__(self):
        self.vertices = {} # why not list? - because key = the word value is the vertex of the word

    def get_vertex_values(self):
        return set(self.vertices.keys())

    def add_vertex(self, value):
        self.vertices[value] = Vertex(value) # powerful: creates vertex and a place for it within the graph

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
