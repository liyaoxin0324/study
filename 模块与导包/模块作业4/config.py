# o确保配置只从文件加载一次，即使模块被多次导入或重载。
# o在主程序中导入 config 模块，调用 get_config() 并打印配置。修改 config.json 文件的内容，
# 尝试在程序中重新获取配置，观察行为（需要用到 importlib.reload）。



import json
import os
from 模块作业4 import config
_config = None
def getconfig():
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, "config.json")
    global _config
    if _config is None:
        with open(file_path, "r", encoding="utf-8") as f:
            _config = json.load(f)
    return _config



    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # config_file = os.path.join(current_dir, "config.json")
    # with open(config_file, 'r', encoding='utf-8') as f:
    #     config_data = json.load(f)
    #     print(config_data)
    #     return config_data



