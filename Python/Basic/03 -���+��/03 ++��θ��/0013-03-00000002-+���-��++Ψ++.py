# -*- coding: utf-8 -*-
"""
作业2：
现有办公室座位表 seating 如下

先要求从 1号办公室、2号办公室中分别随机抽一个安排到4号办公室去

    1. 随机从1号 2号办公室中选取一个人
    2. 将其安排到4号办公室去
    3. 最后先安排好的座位表打印

"""
import random

seating = [
    ('1号办公室1位置', '戴贵富'),
    ('1号办公室2位置', '田显余'),
    ('1号办公室3位置', '李元东'),
    ('2号办公室1位置', '廖德超'),
    ('2号办公室2位置', '秦代坤'),
    ('2号办公室3位置', '杨久林'),
    ('3号办公室1位置', '邓永明'),
    ('3号办公室2位置', '张勇')
]

# 要求打印可以如下（内容一样）
"""
[
    ('1号办公室1位置', '戴贵富'), ('1号办公室3位置', '李元东'),
    ('2号办公室2位置', '秦代坤'), ('2号办公室3位置', '杨久林'), 
    ('3号办公室1位置', '邓永明'), ('3号办公室2位置', '张勇'), 
    ('4号办公室1位置', '田显余'), ('4号办公室2位置', '廖德超')
]
"""
"""自己在下方编写代码实现功能"""

num = 1
for i in seating:
    if seating[-1][0] == '4号办公室2位置':
        break

    a = random.choice(seating)
    if '3号' in a[0]:
        pass
    else:
        seating.append((f'4号办公室{num}位置', a[1]))
        num += 1
        seating.remove(a)

print(seating)
