class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n) time complexity
        # Hashmap to keep track of value occurences
        count = {}
        
        # An array that is the size of the input array. 
        # The index will be the count of an element
        # The value will be a list of values that occur that much
            # Ex: freq[2] -> returns a list of values that repeat twice
        freq = [[] for i in range(len(nums)+1)]

        # Count how many times a value appears in the input array
        for n in nums:
            count[n] = 1 + count.get(n,0)

        
        for n, c in count.items():
            # c = index
            # "n appeared c number of times"
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res