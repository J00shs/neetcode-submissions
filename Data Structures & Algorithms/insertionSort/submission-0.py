class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        res = []
        if not pairs:
            return res
        for i in range(len(pairs)):
            j = i - 1
            while(j >= 0 and pairs[j+1].key < pairs[j].key):
                tmp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j -= 1
            res.append(pairs.copy())
        return res