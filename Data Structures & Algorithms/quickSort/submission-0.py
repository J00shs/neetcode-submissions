# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
    


    def quickSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        a = s

        for b in range(s, e):
            if arr[b].key < pivot.key:
                tmp = arr[a]
                arr[a] = arr[b]
                arr[b] = tmp
                a += 1
        arr[e] = arr[a]
        arr[a] = pivot

        self.quickSortHelper(arr, s, a - 1)
        self.quickSortHelper(arr, a + 1, e)
            
        