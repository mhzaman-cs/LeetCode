class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []

        l = len(words[0])
        d = {}
        for w in words:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1
        i = 0
        ans = []

        for k in range(l):
            left = k
            subd = {}
            count = 0
            for j in range(k, len(s)-l+1, l):
                tword = s[j:j+l]
                # valid word
                if tword in d:
                    if tword in subd:
                        subd[tword] += 1
                    else:
                        subd[tword] = 1
                    count += 1
                    while subd[tword] > d[tword]:
                        subd[s[left:left+l]] -= 1
                        left += l
                        count -= 1
                    if count == len(words):
                        ans.append(left)
                # not valid
                else:
                    left = j + l
                    subd = {}
                    count = 0

        return ans




class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return node
        m, visited, stack = dict(), set(), deque([node])
        while stack:
            n = stack.pop()
            if n in visited:
                continue
            visited.add(n)
            if n not in m:
                m[n] = Node(n.val)
            for neigh in n.neighbors:
                if neigh not in m:
                    m[neigh] = Node(neigh.val)
                m[n].neighbors.append(m[neigh])
                stack.append(neigh)
        return m[node]
