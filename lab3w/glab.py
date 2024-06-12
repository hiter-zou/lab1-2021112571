import re
import networkx as nx
import logging



def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
    return text

def process_text(text):
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    return words

def create_graph(words):
    G = nx.DiGraph()
    for i in range(len(words) - 1):
        if G.has_edge(words[i], words[i+1]):
            G[words[i]][words[i+1]]['weight'] += 1
        else:
            G.add_edge(words[i], words[i+1], weight=1)
    return G


def find_bridge_words(G, word1, word2):
    if word1 not in G and word2 not in G:
        print(f"No {word1} and {word2} in the graph!")
        return False
    if word1 not in G:
        print(f"No {word1} in the graph!")
        return False
    if word2 not in G:
        print(f"No {word2} in the graph!")
        return False

    bridge_words = [node
                    for node in G
                    if G.has_edge(word1, node) and G.has_edge(node, word2)]

    if not bridge_words:
        print(f"No bridge words from {word1} to {word2}!")
        return False
    else:
        bridge_words_str = ', '.join(bridge_words[:-1]) + ', and ' + bridge_words[-1]\
            if len(bridge_words) > 1 else \
        bridge_words[0]
        print(f"The bridge words from {word1} to {word2} are: {bridge_words_str}.")
        return bridge_words


def main():
    file_path = "text.txt"
    text = read_file(file_path)
    words = process_text(text)
    G = create_graph(words)
    word1 = "to"
    word2 = "out"
    find_bridge_words(G, word1, word2)



if __name__ == "__main__":
    main()
