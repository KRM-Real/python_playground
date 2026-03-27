# 1054. Distant Barcodes
# In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].
# Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

# Example 1:
# Input: barcodes = [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]

import heapq
from collections import Counter, deque, namedtuple


def rearrangeBarcodes(self, barcodes):
        counter = Counter(barcodes)
        counter = [[-value, key] for key, value in counter.items()]
        
        heapq.heapify(counter)
        item = heapq.heappop(counter)
        ret = [None] * len(barcodes)
        
        for i in range(len(barcodes)):
            item[0] += 1
            ret[i] = item[1]
            if counter:
                item = heapq.heapreplace(counter, [item[0], item[1]])
            
        return ret