import heapq


class Node:
    def __init__(self, char, freq, left, right):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __repr__(self):
        # return ("(C:{} F:{} )".format(self.char, self.freq))
        return ("(C:{} F:{} L:{} R:{})".format(self.char, self.freq, self.left, self.right))

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def __init__(self, chars, freq):
        self.nodes = []
        for i in range(len(freq)):
            self.nodes.append(Node(chars[i], freq[i], None, None))
        # print(self.nodes)

    def encode(self):
        minHeap = self.nodes
        heapq.heapify(minHeap)

        # till we have one root node
        while len(minHeap) > 1:
            l = heapq.heappop(minHeap)
            r = heapq.heappop(minHeap)
            _node = Node(" ", l.freq + r.freq, l, r)
            heapq.heappush(minHeap, _node)
        root = heapq.heappop(minHeap)
        self.print_(root, '')

    def print_(self, node, s):
        # print(node)

        if node.left == None and node.right == None and node.char != " ":
            print(node.char + " " + s)
            return
        self.print_(node.left, s + '0')
        self.print_(node.right, s + '1')


chars = ['a', 'b', 'c', 'd', 'e', 'f']
freqs = [5, 9, 12, 13, 16, 45]
h = Huffman(chars, freqs)
h.encode()
