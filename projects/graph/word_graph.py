import string
from graph import Graph
f = open('words.txt', 'r')
words_list = set(f.read().split("\n"))
f.close()
words_set = set(words_list)
alphabet = list(string.ascii_lowercase)

def shortest_word_transformation(starting_word, ending_word):
    graph = Graph()
    graph_words = set()
    for i in range(len(starting_word)):
        for letter in alphabet:
            test_list = list(starting_word)
            test_list[i] = letter
            test_word = "".join(test_list)
            if test_word in words_set:
                graph_words.add(test_word)
                graph.add_vertex(test_word)
    for i in range(len(ending_word)):
        for letter in alphabet:
            test_list = list(ending_word)
            test_list[i] = letter
            test_word = "".join(test_list)
            if test_word in words_set:
                graph_words.add(test_word)
                graph.add_vertex(test_word)
    for word in graph_words:
        for check_word in graph_words:
            if sum(a != b for a, b in zip(word, check_word)) == 1:
                graph.add_edge(word, check_word)
    return graph.bfs(starting_word, ending_word)
            
print(shortest_word_transformation('hit', 'cog'))
