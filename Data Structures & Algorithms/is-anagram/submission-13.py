class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = [0] * 26

        for char in s :
            idx = ord(char) - ord('a')

            freq[idx]+=1

        for char in t :
            idx = ord(char) - ord('a')

            freq[idx]-=1

            if freq[idx] < 0 :
                return False

        return True
        