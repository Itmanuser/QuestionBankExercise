"""
百鸡问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""
while True:
    try:
        n = int(input())
        for i in range(100):
            for j in range(100-1):
                if 5*i + 3*j + (100-i-j)/3 == 100:
                    print(i,j, 100-i-j)
    except:
        break