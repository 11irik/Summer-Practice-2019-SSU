# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

nums = list(map(float, input().split()))

for i in range(1, len(nums) - 1):
    if nums[i-1] % 2 == 0 and nums[i+1] % 2 == 0:
        nums[i] = 0

print(*nums)

#5.2