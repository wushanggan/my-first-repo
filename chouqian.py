# -*- coding: utf-8 -*-
# =====================================================================
# 随机点名器（feature-count 版）
# 功能：输入名单 → 每次按回车抽一个 → 抽中的人移出池子 → 显示第几次抽签
# =====================================================================

import random  # 导入 random（随机）模块

print("=" * 40)  # 打印分隔线
print("      欢迎使用「随机点名器」")  # 欢迎语
print("=" * 40)

while True:  # 循环：直到用户输入了有效名单
    text = input("请输入名字（用空格或逗号分开）：")  # 读入一串名字
    text = text.replace("，", " ")  # 中文逗号换空格
    text = text.replace(",", " ")  # 英文逗号换空格
    text = text.replace("、", " ")  # 中文顿号换空格
    names = text.split()  # 切成名字列表
    if len(names) == 0:  # 什么都没输入
        print("你还没有输入名字，请重新输入～")
        continue  # 重新提问
    break  # 名单有效，往下走

count = 0  # 抽签次数计数器
while len(names) > 0:  # 池子里还有人就继续抽
    input("按回车开始第 %d 次抽签……" % (count + 1))  # 等用户按回车
    count = count + 1  # 次数加 1
    winner = random.choice(names)  # 从池子里随机挑一个
    names.remove(winner)  # 抽中的人移出池子，不会重复
    print("第 %d 次抽签，被点到的是：%s" % (count, winner))  # 报结果
    print("（池子里还剩 %d 个人）" % len(names))  # 报剩余

print("所有名字都抽过了，抽签结束～")