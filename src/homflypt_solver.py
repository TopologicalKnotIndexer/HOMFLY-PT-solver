# 给定扭结的 PD_CODE，计算扭结的 HOMFLY_PT 多项式
# 需要注意的是，HOMFLYPT 多项式的计算在计算 crossing 数很多的扭结时可能会崩溃

import sys
from de_r1_k8           import de_r1_k8
from sage_run_interface import sage_run

CODE_TEMPLATE = """
from sage.all import *
K = Knot(<<<PD_CODE>>>) # Knot PD_CODE
K3a1 = Knot([[1, 5, 2, 4], [3, 1, 4, 6], [5, 3, 6, 2]])
if str(K3a1.homfly_polynomial()).strip() == "L^-2*M^2 - 2*L^-2 - L^-4":
    K = K.mirror_image()
print(K.homfly_polynomial())
"""

# 根据 PD_CODE 计算镜像扭结的 homflypt 多项式
def homflypt_solver(pd_code: list) -> str:
    pd_code   = de_r1_k8(pd_code)
    sage_code = CODE_TEMPLATE.replace("<<<PD_CODE>>>", str(pd_code))
    exit_code, stdout_ans, stderr_ans = sage_run(sage_code)
    if exit_code != 0:
        sys.stderr.write(stderr_ans)                     # 输出错误信息
        raise AssertionError("sage_run: exit_code != 0") # 抛出异常
    return stdout_ans.strip()                            # 保证首尾没有空白字符

if __name__ == "__main__": # 测试
    print(homflypt_solver([[1, 5, 2, 4], [3, 7, 4, 6], [5, 3, 6, 2], [7, 10, 8, 11], [9, 12, 10, 1], [11, 8, 12, 9]]))