# HOMFLY-PT-solver
给定 PD_CODE，计算其镜像扭结的 HOMFLY-PT 多项式的值。



## 前置条件

- `sage` https://github.com/sagemath/sage
- `python3`



## 运行方式

- `python3 ./src/main.py`
  - 向标准输入写入一个 list of list 作为 PD_CODE
  - 程序会将该 PD_CODE 对应扭结的 HOMFLY-PT 多项式输出到标准输出
