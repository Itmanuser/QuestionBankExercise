# 求输入A和B的最小公倍数
def get_min_doubule(a,b):
    x = min(a,b)
    y = max(a,b)
    for i in range(1,y+1):
        if x*i%y == 0:
            print(x*i)
            break
 
if __name__ == "__main__":
    while True:
        try:
            a,b = map(int, input().split(" "))
            get_min_doubule(a, b)
        except:
            break