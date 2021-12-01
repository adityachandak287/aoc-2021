nums = []
with open("01/input") as file:
    nums = [int(x) for x in file.readlines()]

count = 0
[a,b,c] = nums[:3]
prevSum = a + b + c
N = len(nums)
for idx in range(len(nums) - 2):
    if idx == 0:
        continue
    d = nums[idx+2]
    currSum = prevSum - a + d
    if currSum > prevSum:
        count+=1
    prevSum = currSum
    a = b
    b = c
    c = d

print(count)
