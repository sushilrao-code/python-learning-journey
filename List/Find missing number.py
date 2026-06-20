# nums = [1, 2, 3, 5, 6, 8]
# n = len(nums) + 1
# expexted = n * (n + 1) // 2
# actual = 0
# for i in nums:
#     actual+=i

# print("Missing",expexted - actual)
nums = [1, 2, 3, 5, 6, 8]
for i in range(1,max(nums)+1):
    if i not in nums:
        print("Missing",i)