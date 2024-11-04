import random
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent={}
        self.neighbours=[]
        self.neighbours_weights=[]
    
    def add_edge_to(self, target, weight=0):
        self.adjacent[target] = weight
    
    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def probability_map(self):
        for (word, weight) in self.adjacent.items():
            self.neighbours.append(word)
            self.neighbours_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbours, weights =  self.neighbours_weights)[0]

class Graph:
    def __init__(self):
        self.vertices={}

    def get_all_words(self):
        return set(self.vertices.keys())
    
    def add_word(self, word):
        self.vertices[word] = Vertex(word)
    
    def get_value(self, word):
        if word not in self.vertices:
            self.add_word(word)
        return self.vertices[word]
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()
    
    def get_probability_mappings(self):
        for  vertex in self.vertices.values():
            vertex.probability_map()