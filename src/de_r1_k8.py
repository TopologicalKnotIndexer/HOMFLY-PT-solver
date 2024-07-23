# 桥接：https://github.com/TopologicalKnotIndexer/pd_code_de_r1_k8
import os
DIRNOW = os.path.dirname(os.path.abspath(__file__))
SUBDIR = os.path.join(DIRNOW, "pd_code_de_r1_k8", "src") # 子包路径

# ======================================== BEGIN IMPORT FROM PATH ======================================== #
import importlib
import json
import sys
def load_module_from_path(path: str, mod_name: str): # 从指定路径导入一个包
    assert os.path.isdir(path)                       # 路径必须存在
    path         = os.path.abspath(path)             # 获得绝对路径
    old_sys_path = json.loads(json.dumps(sys.path))  # 存档旧的 sys.path
    sys.path     = [path] + sys.path                 # 将新的路径加入 sys.path
    mod          = importlib.import_module(mod_name) # 加载指定的包
    sys.path     = old_sys_path                      # 恢复旧的 sys.path
    return mod
# ======================================== END IMPORT FROM PATH ======================================== #

def de_r1_k8(pd_code: list) -> list:
    return load_module_from_path(SUBDIR, "main").de_r1_k8(pd_code)

if __name__ == "__main__": # 测试
    print(de_r1_k8([[1, 2, 2, 1]]))