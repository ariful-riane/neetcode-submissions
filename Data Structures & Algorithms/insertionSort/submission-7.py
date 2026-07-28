# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        l = []
        if pairs:
            l.append(pairs[:])
            for i in range(1, len(pairs)):
                c = pairs[i]
                c_key = c.key
                j = i - 1

                while j >= 0 and pairs[j].key > c_key:
                    pairs[j + 1] = pairs[j]
                    j -= 1

                pairs[j + 1] = c
                l.append(pairs[:])
        
        return l