class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create the hashmap
        # Mapping charCount to the list of anagrams
        res = defaultdict(list)

        for s in strs:
            # Create an array with 26 characters (a-z)
            count = [0] * 26

            # For each letter in a string
            for c in s:
                # How can we map a to index 0 and z to index 25?
                # Take the ASCII value of each character - ASCII value of a

                # Example:
                # a = 97
                # b = 98
                # 98 - 97 = 1
                # Therefore, b is stored at index 1
                count[ord(c) - ord("a")] += 1

            # Use the completed character count as the key
            # Why did we use tuple()?
                # Lists cannot be keys b/c lists are mutable
                # Mutable meaning it can be changed after being creation
                # If a key changes after insertion, it can cause lookup issues. 
            res[tuple(count)].append(s)

        return list(res.values())

        # O(m * n) solution
        # m = number of strings given
        # n = average number of characters in each string