# 問題一 

def calculate(min, max):
# 請用你的程式補完這個函式的區塊
    sum=0
    for i in range(min,max+1):
        sum+=i
    print(sum)

calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


# --------------------------------------------------------------------------------------------------------


# 問題二

def avg(data):
# 請用你的程式補完這個函式的區塊
    count = int(data['count'])
    totalNum = 0
    for value in data['employees']:
        totalNum = totalNum + value['salary']

    print(totalNum/count)

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        },
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }
    ]
}) # 呼叫 avg 函式


# --------------------------------------------------------------------------------------------------------


# 問題三

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


# --------------------------------------------------------------------------------------------------------


# 問題四

def twoSum(nums, target):
    length=len(nums)
    numsList= []
    for i in range(length):
        for j in range(1,length):
            sumNum = nums[i] + nums[j]
            if sumNum == target:
                numsList.append(i)
                numsList.append(j)
                return(numsList)

result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9


# --------------------------------------------------------------------------------------------------------


# 問題五

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




