class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True


    def search(self, word: str) -> bool:
        
        def dfs(j, root): 
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    # Go through characters available of current root
                    for child in curr.children.values(): 
                        # Explore remainder of the word starting from child
                        if dfs(i+1, child): 
                            return True
                    # If no child path match the rest of word
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            # After checking all characters, True if we are at valid end of word
            return curr.word
            
        return dfs(0, self.root)
    
        
