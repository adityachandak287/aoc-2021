nums = []
with open("01/input") as file:
    nums = [int(x) for x in file.readlines()]

count = 0
prev = nums[0]
for num in nums[1:]:
    if num > prev:
        count+=1
    prev = num

print(count)
