class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for i in range(length):

            for j in range(length):

                if (i==j):
                    j+=1

                temp = nums[i] + nums[j]

                if (temp == target):
                    return[i,j]
                else:
                    j+=1
                
                if(i==j):
                    j+=1

                if(i==j) and (j==length):
                    return 0
