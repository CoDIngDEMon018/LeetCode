class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        r=0
        # l=0
        res=0
        for i in range(len(nums)):
            while r<=i and nums[i]-nums[r]>1:
                r+=1
            if nums[i]-nums[r]==1:
                res=max(res,i-r+1)
        return res