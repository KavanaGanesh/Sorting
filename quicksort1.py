from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.qsort(pairs, 0, len(pairs)-1)
        return pairs

    def qsort(self, pairs, start, end):
        if end - start + 1 <= 1:
            return 
        
        store = start
        pivot = pairs[end]


        for i in range(start, end):
            if pairs[i][0] < pivot[0]:
                temp = pairs[store]
                pairs[store] = pairs[i]
                pairs[i] = temp
                store = store + 1

        pairs[end] = pairs[store]
        pairs[store] = pivot

        self.qsort(pairs, start, store - 1)
        self.qsort(pairs, store + 1, end)


if '__name__ = __main__':
    pairs = [(3, "cat"), (2, "dog"), (3, "bird")]
    print(Solution().quickSort(pairs))

