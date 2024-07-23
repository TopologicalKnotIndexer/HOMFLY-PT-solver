# 从标准输入读入一个 PD_CODE
# 将 HOMFLY-PT 多项式输出到标准输出

import sys
from homflypt_solver import homflypt_solver
from input_sanity    import input_sanity

def main():
    input_pdcode = sys.stdin.read().strip()   # 输入字符串
    pd_code      = input_sanity(input_pdcode) # 检查是否是合法的 PD_CODE
    print(homflypt_solver(pd_code))           # 输出 homflypt 多项式

if __name__ == "__main__":
    main()