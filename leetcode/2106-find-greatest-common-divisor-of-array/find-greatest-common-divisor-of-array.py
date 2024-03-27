class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minim = min(nums)
        maxim = max(nums)
        while maxim !=0:
            rem = minim % maxim
            minim = maxim
            maxim = rem
        return minim
