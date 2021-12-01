import sys

nums = [int(x) for x in sys.stdin.readlines()]

count = 0
prev = nums[0]
for num in nums[1:]:
    if num > prev:
        count+=1
    prev = num

print(count)
