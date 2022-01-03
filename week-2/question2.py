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
