import time

# 获取当前时间
now = time.localtime()

# 将时间格式化为字符串
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S.%z", now)

# 输出格式化后的时间字符串
print(formatted_time)