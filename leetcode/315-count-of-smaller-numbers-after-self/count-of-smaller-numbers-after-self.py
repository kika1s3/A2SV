from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        output = []
        s = SortedList()
        for num in nums[::-1]:
            ans = bisect_left(s, num)
            s.add(num)
            output.append(ans)
        return reversed(output)