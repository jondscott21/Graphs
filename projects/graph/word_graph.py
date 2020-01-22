import string
from graph import Graph
from util import Queue

f = open('words.txt', 'r')
words_list = set(f.read().split())
f.close()

words_set = set()
for word in words_list:
    words_set.add(word.lower())

alphabet = list(string.ascii_lowercase)

queue = Queue()
graph = Graph()
def find_words(word, graph_words=None):
    # neighbors = []
    for i in range(len(word)):
        for letter in alphabet:
            test_list = list(word)
            test_list[i] = letter
            test_word = "".join(test_list)
            if test_word is not word and test_word in words_set:
                graph_words.add(test_word)
                graph.add_vertex(test_word)
                # neighbors.append(test_word)
    # return neighbors

def shortest_word_transformation(starting_word, ending_word):
    # print('sail' in words_list)
    if ending_word not in words_set:
        return "ending word is not in the word list"
    if len(starting_word) != len(ending_word):
        return 'Word lengths do not match'
    graph_words = set()
    graph_words.add(starting_word)
    for i in range(len(starting_word)):
        for letter in alphabet:
            test_list = list(starting_word)
            test_list[i] = letter
            test_word = "".join(test_list)
            if test_word in words_set:
                graph_words.add(test_word)
                graph.add_vertex(test_word)
            find_words(test_word, graph_words)
    for i in range(len(ending_word)):
        for letter in alphabet:
            test_list = list(ending_word)
            test_list[i] = letter
            test_word = "".join(test_list)
            if test_word in words_set:
                graph_words.add(test_word)
                graph.add_vertex(test_word)
            find_words(test_word, graph_words)
    for word in graph_words:
        for check_word in graph_words:
            if sum(a != b for a, b in zip(word, check_word)) == 1:
                graph.add_edge(word, check_word)

    # for w in words_set:
    #     if len(w) == len(starting_word):
    #         graph_words.add(w)
    #         graph.add_vertex(w)
    # for word in graph_words:
    #     for check_word in graph_words:
    #         if sum(a != b for a, b in zip(word, check_word)) == 1:
    #             graph.add_edge(word, check_word)
    return graph.bfs(starting_word, ending_word)
            
# ['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
# print(shortest_word_transformation('hit', 'cog'))
# print(shortest_word_transformation('sail', 'boat'))
print(shortest_word_transformation('achen', 'sabik'))
