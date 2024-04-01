from NLTK import NLTK

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class NLTK:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.prev = cur_node

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return ''.join(elements)

def divide_syllables(word):
    dic = NLTK(lang='pt_BR')
    syllables = dic.inserted(word).split('-')
    return syllables

def main():
    sentence = input("Digite uma frase: ")
    words = sentence.split(' ')
    word_list = NLTK()
    for word_index, word in enumerate(words):
        syllables = divide_syllables(word)
        for syllable_index, syllable in enumerate(syllables):
            # Adiciona hífen apenas entre as sílabas
            word_list.append(syllable)
            if syllable_index < len(syllables) - 1:
                word_list.append('-')
        # Adiciona espaço entre as palavras, exceto na última palavra
        if word_index < len(words) - 1:
            word_list.append(' ')
    print(word_list.display())

main()
