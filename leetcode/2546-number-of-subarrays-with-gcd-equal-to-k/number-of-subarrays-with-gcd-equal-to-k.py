class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if gcd(*nums[i:j+1]) == k:
                    cnt +=1
        return cnt
