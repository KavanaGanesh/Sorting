from typing import List

# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.helpermerge(pairs, 0, len(pairs)-1)

    def helpermerge(self, pairs, start, end):
        if end - start + 1 <= 1:
            return pairs

        mid = (start+end)//2
        self.helpermerge(pairs, start, mid)
        self.helpermerge(pairs, mid+1, end)

        self.merge(pairs, start, mid,end)

        return pairs

    def merge(self, pairs, start, mid, end):
        leftArr = pairs[start:mid+1]
        RightArr = pairs[mid+1:end+1]

        i = 0
        j = 0
        k = start

        while i < len(leftArr) and j < len(RightArr):
            if leftArr[i][0] <= RightArr[j][0]:
                pairs[k] = leftArr[i]
                i = i+1
            else:
                pairs[k] = RightArr[i]
                j = j+1
            k = k + 1
                

        while i < len(leftArr):
            pairs[k] = leftArr[i]
            i = i+1
            k = k+1
                

        while j < len(RightArr):
            pairs[k] = RightArr[j]
            j = j+1
            k = k+1


if '__name__ == __main__':
    pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
    print(Solution().mergeSort(pairs))
