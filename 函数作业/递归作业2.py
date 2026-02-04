# # 题目2：使用递归解决汉诺塔问题 (Tower of Hanoi)
# # 有三根柱子，要把一堆盘子从 A 移到 C，大盘子不能压在小盘子上。
# # 逻辑：把上面 n-1 个盘子从 A 移到 B。把最底下的盘子从 A 移到 C。
# # 把 B 上的 n-1 个盘子移到 C。
def hanoi_tower(n,y,f,m,a_list,b_list,c_list):
    count = 0
    if n==1:
        if y == 'A':
            pan = a_list.pop()  # pop()从尾部取（大盘在列表底，小盘在顶，符合物理堆叠）
        elif y == 'B':
            pan = b_list.pop()
        else:
            pan = b_list.pop() if y == 'B' else c_list.pop()
        if m == 'A':
            a_list.append(pan)
        elif m == 'B':
            b_list.append(pan)
        else:
            c_list.append(pan)
        print(f"盘子{pan}从 {y}{eval(y.lower() + '_list')} >> {m}{eval(m.lower() + '_list')}")
        return count + 1
    else:
        count += hanoi_tower(n - 1, y, m, f, a_list, b_list, c_list)
        if y == 'A':
            pan = a_list.pop()
        elif y == 'B':
            pan = b_list.pop()
        else:
            pan = c_list.pop()

        if m == 'A':
            a_list.append(pan)
        elif m == 'B':
            b_list.append(pan)
        else:
            c_list.append(pan)
        print(f"盘子{pan}从 {y}{eval(y.lower() + '_list')} >> {m}{eval(m.lower() + '_list')}")
        count += 1
        # 步骤3：n-1个盘子从辅助柱→目标柱，源柱作为临时辅助（核心：切换递归参数）
        count += hanoi_tower(n - 1, f, y, m, a_list, b_list, c_list)
        return count
n_input = int(input("请输入盘子的数量（最好不要超过15）："))
a_list= list(range(n_input,0,-1))
b_list = []
c_list = []
actual_count = hanoi_tower(n_input, 'A', 'B', 'C', a_list, b_list, c_list)
# 保留原代码的结果打印格式，补充实际移动次数
print("-" * 40)
print(f"理论最小移动次数: {2**n_input - 1}")
print(f"实际移动次数: {actual_count}")
print(f"最终状态: A{a_list} B{b_list} C{c_list}")



