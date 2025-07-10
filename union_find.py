class UnionFind:

    def __init__(self, n):
        # Elements are united if they have the same root parent.
        self._parents = list(range(n))
        # Ranking helps to lower the tree height.
        self._ranks = [1] * n

   def find(self, i):
        while i != self._parents[i]:
            self._parents[i] = self._parents[self._parents[i]]
            i = self._parents[i]
        return i

    def union(self, i, j):
        ip = self.find(i)
        jp = self.find(j)
        if ip == jp:
            return

        ir = self._ranks[ip]
        jr = self._ranks[jp]
        # If the rank of i's root parent is heigher, it means the root parent has more elements
        # and we don't want to make its tree heigher.
        if ir > jr:
            self._parents[jp] = ip
            self._ranks[ip] += self._ranks[jp]
        else:
            self._parents[ip] = jp
            self._ranks[jp] += self._ranks[ip]
