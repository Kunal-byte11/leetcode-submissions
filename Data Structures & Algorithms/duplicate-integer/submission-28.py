class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seennums = set()

        for n in nums:
            if n in seennums:
                return True

            else:
                seennums.add(n)
        
        return False
        