class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        prefix = 1
        postfix = 1
        for i in range(1,len(nums)):
            prefix = prefix*nums[i-1]
            output[i] = prefix
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix = 1
            else:
                postfix = postfix*nums[i+1]
            final = postfix*output[i]
            output[i] = final
        return output


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while right >= left :
            if numbers[left] + numbers[right] == target :
                return [left+1,right+1]
            if numbers[left] + numbers[right] > target :
                right -= 1
            if numbers[left] + numbers[right] < target :
                left += 1

        

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        fmap = {}
        for i in range(len(nums)):
            if nums[i] in fmap:
                fmap[nums[i]] += 1
            else:
                fmap[nums[i]] = 1
        index = 0
        for i in range(3):
            if i in fmap:
                for j in range(fmap[i]):
                    nums[index] = i
                    index += 1

