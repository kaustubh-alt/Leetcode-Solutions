class Solution:
    def firstMissingPositive(self, nums) -> int:
        if 1 not in nums:
            return 1
        maa = max(nums)
        nums = list(set(nums))
        sotnum = sorted([x for x in nums if x > 0])
        for i in range(1,len(sotnum)):            
            if (sotnum[i] - sotnum[i-1]) <= 1:
                continue
            else:
                return sotnum[i-1]+1
                break
                
        return maa+1
