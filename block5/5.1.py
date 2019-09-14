# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

nums = list(map(float, input().split()))

min = nums[0]
max = nums[0]
minPos = 0
maxPos = 0

for i in range(len(nums)):
    if nums[i] > max:
        maxPos = i
        max = nums[i]
    elif nums[i] < min:
        minPos = i
        min = nums[i]

if minPos > maxPos:
    j = minPos
    minPos = maxPos
    maxPos = j

product = 1
for i in range(minPos + 1, maxPos):
    product *= nums[i]
print(product)
