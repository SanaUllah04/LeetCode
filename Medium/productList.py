nums = [1, 2, 3, 4]

answer = [1] * len(nums)

print(answer)

# Loop 1: Product of everything to the LEFT
prefix = 1
for i in range(len(nums)):
    answer[i] = prefix
    prefix *= nums[i]

# Loop 2: Product of everything to the RIGHT
suffix = 1
for i in range(len(nums) - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]

print(answer)
# Output: [24, 12, 8, 6]