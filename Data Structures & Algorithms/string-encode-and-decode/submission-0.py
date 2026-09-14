class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Capture the integer
            # Go up until we hit our delimiter, #
            while s[j] != "#":
                j += 1
            # from i until index j, but not includding index j
            length = int(s[i:j])
            # Go from the the start of the word to the end
            res.append(s[j+1 : j + 1 + length])
            i = j + 1 + length
        return res


