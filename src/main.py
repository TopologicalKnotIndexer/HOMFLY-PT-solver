# 从标准输入读入一个 PD_CODE
# 将 HOMFLY-PT 多项式输出到标准输出

import sys
from homflypt_solver import homflypt_solver

def main():
    input_pdcode = eval(sys.stdin.read().strip())
    print(homflypt_solver(input_pdcode))

if __name__ == "__main__":
    main()