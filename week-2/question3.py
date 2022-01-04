def maxProduct(nums):
# 請用你的程式補完這個函式的區塊

    length = len(nums)
    productList = list()
    for i in range(length):
        for j in range(i + 1, length):
            total = nums[i] * nums[j]
            productList.append(total)

    maxNum = max(productList)
    print(maxNum)


maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2
