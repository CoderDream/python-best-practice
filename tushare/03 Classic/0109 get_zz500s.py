import tushare as ts

# 中证500成份股
# 获取中证500成份股
#
# 返回值说明：
#
# code：股票代码
# name：股票名称

df = ts.get_zz500s()
print(df)

#           date    code  name  weight
# 0   2019-09-30  600006  东风汽车    0.10
# 1   2019-09-30  600008  首创股份    0.20
# 2   2019-09-30  600017   日照港    0.14
# 3   2019-09-30  600021  上海电力    0.22
# 4   2019-09-30  600022  山东钢铁    0.25
# ..         ...     ...   ...     ...
# 495 2019-09-30  300376   易事特    0.11
# 496 2019-09-30  300383  光环新网    0.45
# 497 2019-09-30  300418  昆仑万维    0.19
# 498 2019-09-30  300450  先导智能    0.47
# 499 2019-09-30  300459  金科文化    0.08
#
# [500 rows x 4 columns]

