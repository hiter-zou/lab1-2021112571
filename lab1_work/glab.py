import re
import networkx as nx
import matplotlib.pyplot as plt
import random
import tkinter as tk
import time


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
        if G.has_edge(words[i], words[i + 1]):
            G[words[i]][words[i + 1]]['weight'] += 1
        else:
            G.add_edge(words[i], words[i + 1], weight=1)
    return G


def showDirectedGraph(G):
    #可改进成没有交叉边的算法
    pos = nx.spectral_layout(G)
    pos = nx.spring_layout(G, pos=pos, k=0.5, iterations=100)
    nx.draw(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.savefig('Gpng')
    plt.show()


def find_bridge_words(G, word1, word2, is_print=True):
    if word1 not in G and word2 not in G:
        if is_print:
            print(f"No {word1} and {word2} in the graph!")
        return False
    if word1 not in G:
        if is_print:
            print(f"No {word1} in the graph!")
        return False
    if word2 not in G:
        if is_print:
            print(f"No {word2} in the graph!")
        return False
    bridge_words = [node for node in G if G.has_edge(word1, node) and G.has_edge(node, word2)]
    if not bridge_words:
        if is_print:
            print(f"No bridge words from {word1} to {word2}!")
        return False
    if is_print:
        print(f"The bridge words from {word1} to {word2} are: {bridge_words[-1]}.")
    return bridge_words[-1]


def generateNewText(G, text):
    words = process_text(text)
    new_text = words[0]
    for i in range(len(words) - 1):
        bridge_words = find_bridge_words(G, words[i], words[i + 1], is_print=False)
        if bridge_words:
            new_text += " " + bridge_words
        new_text += " " + words[i + 1]
    return new_text


def calcShortestPath(G, word1, word2):
    if word1 not in G and word2 not in G:
        print(f"No {word1} and {word2} in the graph!")
        return None
    if word1 not in G:
        print(f"No {word1} in the graph!")
        return None
    if word2 not in G:
        print(f"No {word2} in the graph!")
        return None
    try:
        path = nx.shortest_path(G, source=word1, target=word2)
    except nx.NetworkXNoPath:
        print(f"No path from {word1} to {word2}!")
        return None
    result = " -> ".join(path)
    return result


def randomWalk(G, text_widget, stop_event):
    is_stop = False
    start = random.choice(list(G.nodes))
    sentence = [start]
    text_widget.insert(tk.END, start + " ")
    while not is_stop:
        if not list(G[start]):
            text_widget.insert(tk.END, "\n\nNext not found. Random walk stopped.\n\n\n\n\n")
            break
        next = random.choice(list(G[start]))
        if next in sentence:
            text_widget.insert(tk.END, "\n\nLoop detected. Random walk stopped.\n\n\n\n\n")
            break
        sentence.append(next)
        text_widget.insert(tk.END, next + " ")
        start = next
        # 检查停止事件
        time.sleep(1)
        if stop_event.is_set():
            text_widget.insert(tk.END, "\n\nStop.\n\n\n\n\n")
            is_stop = True


def main():
    file_path = "text.txt"
    text = read_file(file_path)
    words = process_text(text)
    G = create_graph(words)
    showDirectedGraph(G)
    word1 = input("请输入第一个单词：")
    word2 = input("请输入第二个单词：")
    if find_bridge_words(G, word1, word2):
        pass
    text = "Seek to explore new and exciting synergies"
    new_text = generateNewText(G, text)
    print(new_text)
    path = calcShortestPath(G, "to", "new")
    if path:
        print(path)
    while True:
        randomWalk(G)


if __name__ == "__main__":
    main()
