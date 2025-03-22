class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            res.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res 
        

        # prefix and postfix sum my version
        # n = len(nums)

        # pref = [1] * n
        # post = [1] * n
        # result = [1] * n

        # for i in range(1,n):
        #     val = nums[i-1] * pref[i-1]
        #     pref[i] = val

        # for j in range(n-2, -1, -1):
        #     val = nums[j+1] * post[j+1]
        #     post[j] = val

        # for k in range(n):
        #     result[k] = pref[k]*post[k]

        # return result





        # Brute force but O(n^2)
        # result = list()
        # for i in range(len(nums)):
        #     sum = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         sum = sum*nums[j]   
        #     result.append(sum)
        # return result
        # --------------------------------
                

        