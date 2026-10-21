nums = [1, 2, 3, 4]

def doubleLoops(nums):

    xly = 1
    answer = [1] * len(nums)

    for i in range(len(nums)):
        target = nums[i]

        for j in range(len(nums)):

            if nums[j] == target:
                j+=1
                pass

            else:
                xly *= nums[j]

        answer[i] = xly
        xly = 1
        print("I am answers = ",answer[i])
    return answer

print(doubleLoops(nums))
        