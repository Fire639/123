import random
n = random.randint(1,10)
a = int(input("不妨猜一下我心里面想的什么数字吧"))
if a == n:
    print("猜对了")
else:
    while a != n:
        a = int(input("猜错了，请重新猜吧"))
        if a == n:
            print('哇草，你是天才吗？')
            break
        else:
            if a > n:
                print('哥，大了大了')
            else:
                print('嘿，小了小了！！')
    print('游戏结束，不玩了~~~')
