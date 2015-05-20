# -*- coding:utf-8 -*-
##########猜数字游戏##########
print '您共有8次答题机会'
import random
i=(random.randrange(0,10))
s=0
for s in range (0,8):
    s +=1
    a = int(raw_input('请输入您的答案:'))
    if i==a:
        print '恭喜你答案正确'
        break
    else:
        print '答案错误,您还有答题机会:',8-s
print '答题结束(*_*)' 





