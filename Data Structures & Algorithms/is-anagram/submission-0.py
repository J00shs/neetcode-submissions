class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # How can I initiate a simple hashmap?
        # Initiating a Hashmap
        s_counts = {}
        t_counts = {}


        for char in s:
            s_counts[char] = s_counts.get(char, 0) + 1
        for char in t:
            t_counts[char] = t_counts.get(char, 0) + 1

        # How can I compare two hashmaps with one another?

        if s_counts == t_counts:
            return True
        return False





        