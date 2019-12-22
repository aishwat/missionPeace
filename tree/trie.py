class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.createNode()

    def createNode(self):
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pointer = self.root

        for level in range(len(key)):
            index = self.charToIndex(key[level])
            if not pointer.children[index]:
                pointer.children[index] = self.createNode()
            #     pointer = pointer.children[level]
            # else:
            #     pointer = pointer.children[level]
            pointer = pointer.children[index]  # move pointer to next level

        pointer.isEndOfWord = True

    def search(self, key):
        print(key)
        pointer = self.root

        for level in range(len(key)):
            index = self.charToIndex(key[level])
            if not pointer.children[index]:
                return False
            pointer = pointer.children[index]

        if pointer != None and pointer.isEndOfWord == True:
            return True


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
main()