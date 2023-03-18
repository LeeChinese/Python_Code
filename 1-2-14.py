"""
讲解字符串格式化的课程练习题
"""
# 定义需要的变量
name = "李氏集团"
stock_price = 19.99
stock_code = "008088"
# 股票 价格 每日 增长 因子
stock_price_daily_growth_factor = 1.2
growth_days = 7

print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每天增长系数是：%.1f" % stock_price_daily_growth_factor, "经过%d天的增长后" % growth_days,      
      "股价达到了%.2f元" % (stock_price * stock_price_daily_growth_factor ** growth_days))  # 两个**代表指数