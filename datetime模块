# datetime
from datetime import datetime        # datetime是一个模块， 后面import的是datetime模块中的一个datetime类

now = datetime.now()                 # 获取当前的datetime
dt = datetime(2017, 11, 20, 19, 3)   # 指定年/月/日/小时/分钟/秒..来创建一个datetime对象 


timestamp(时间戳)              # 1970年1月1日 00:00:00 UTC+00:00时区的时刻成为epoch time，记为0
dt.timestamp()                      # datetime转换为timestamp（timestamp是一个浮点数，小数位表示毫秒）
t = 1429417200.0
dt = datetime.fromtimestamp(t)      # timestamp转换为datetime(时区为当前操作系统设定的时区)   本地时间
dt = datetime.utcfromtimestamp(t)    #UTC时间（标准时区   和英国伦敦时间一致  格林尼治平均时）

本地时间转换为UTC时间（datetime有个时区属性tzinfo，utcnow可以获取当前的utc时间）
from datetime import timezone, timedelta
tz_utc_8 = timezone(timedelta(hours=8))        # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8)              # 将时区替换成之前创建的时区

utc_dt = datetime.utcnow.replace(tzinfo=tz_utc_8)       # 先获取当前utc时间，然后转换为想要的任意时区的时间
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))   # 通过astimezone将带时区的datetime转换到任意时区(强调带时区)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')    # str转datetime
now.strftime('%a, %b %d %H:%M')                                       # datetime转str
（https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior）

datetime加减
from datetime import timedetlta
now + timedelta(hours=8, days=1, seconds=1)    
now = timedelta(minutes=20)

datetime指定时区才能表示一个特定的时间，不然则为本地时间
存储datetime最好转换为timestamp再存储（timestamp的值与时区无关）
