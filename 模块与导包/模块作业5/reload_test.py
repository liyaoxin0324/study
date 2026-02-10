# o导入 counter 模块，调用几次 increment()。
# o使用 importlib.reload() 重载 counter 模块。
# o再次调用 increment()。
# o观察并解释输出结果。思考：如何能“重置”计数器？尝试从 sys.modules 中删除 counter 后再导入。

"""

模块作业5
import sys
import importlib
import counter
for i in range(10):
    print(counter.increment())
importlib.reload(counter)
for i in range(10):
    print(counter.increment())
sys.modules.pop("counter")
importlib.reload(counter)




"""


