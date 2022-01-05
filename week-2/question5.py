def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    numList1 = [str(x) for x in nums]
    str1 = "".join(numList1)
    numList2 = str1.split('1')
    maxZeros = max(numList2, key=len, default='')
    length = len(maxZeros)
    print(length)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3
