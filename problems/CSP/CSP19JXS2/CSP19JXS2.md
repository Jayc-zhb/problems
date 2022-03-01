# 题目描述

给定两个下标从 $1$ 到 $n$ 编号的序列 $a_i,b_i$，定义函数 $S(l,r)(1\le l\le r\le n)$ 为：

$$\sum_{i=l}^r a_i\times \sum_{i=l}^r b_i$$

请你求出下列式子的值：

$$\sum_{l=1}^n \sum_{r=l}^n S(l,r)$$

由于答案可能很大，你只需要给出答案模 $10^9+7$ 后的结果。

# 输入格式

第一行一个正整数 $n$ 表示序列长度。  
第二行 $n$ 个正整数表示 $a_i$。  
第三行 $n$ 个正整数表示 $b_i$。

# 输出格式

仅一行一个整数表示答案模 $10^9+7$  后的结果。

# 输入输出样例

```input1
3
2 3 4
3 4 5
```

```output1
244
```

```input2
5
11 22 33 44 55
12 34 56 78 90
```

```output2
201542
```

# 说明/提示

【数据规模】

对于 $20\%$  的数据：$n\le 10$ , $a_i,b_i\le 10$；

对于 $40\%$  的数据：$n\le 200$ , $a_i,b_i\le 100$；

对于 $70\%$  的数据：$n\le 3000$ , $a_i,b_i\le 10^5$；

对于 $100\%$  的数据：$3\le n\le 5\times 10^5$ , $1\le a_i,b_i\le 10^9$。