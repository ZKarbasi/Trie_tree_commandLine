class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = dict()

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a')

# ADD command
    def insert(self, word):
        Currnode = self.root
        for char in word:
            if char in Currnode.children:
                Currnode = Currnode.children[char]
            else:
                new_node = TrieNode(char)
                Currnode.children[char] = new_node
                Currnode = new_node

        Currnode.is_end = True
        Currnode.counter += 1
        return "OK"
        
# find command
    def find(self , word):
        Currnode = self.root
        for char in word:
            if char not in Currnode.children: 
                return False
            Currnode = Currnode.children[char]
        return Currnode.is_end

# startswith command
    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append(prefix + node.char)
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def startswith(self, x):
        self.output = []
        node = self.root
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.dfs(node, x[:-1])
        return self.output
        # Sort
        #return sorted(self.output, key=lambda x: x[1], reverse=False)


t = Trie()
while(True):
    inputString = input()
    # ADD command
    if (inputString.find('add') == 0):
        x = inputString[4:]
        #print(x)
        print(t.insert(x))
    # find command
    elif (inputString.find('find') == 0):
        x = inputString[5:]
        t.find(x)
    # startswith command
    elif (inputString.find('startswith') == 0):
        x = inputString[11:]
        print(t.startswith(x))
    # exite command
    elif (inputString.find('exite') == 0):
        break
    else:
        print("Wrong cammand !!")







