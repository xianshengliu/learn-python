# -*- coding:utf-8 -*-
##########��������Ϸ##########
print '������8�δ������,��ҪŬ����!'
import random
i=(random.randrange(0,10))
s=0
for s in range (0,8):
    s +=1
    a = int(raw_input('���������Ĵ�:'))
    if i==a:
        print '��ϲ�����ȷ,����һ����������!!'
        break
    else:
        print '�𰸴���,�����д������:'
        print '  ',8-s,'��'
print '�������(*_*)' 