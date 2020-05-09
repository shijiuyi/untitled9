import logging
import logging.config

"""logging.info("info")
logging.debug("debug")
logging.warning("warning")
logging.error("error")
logging.critical("critical")"""

"""# 自定义配置
logging.basicConfig(
    # filename：用指定的文件名创建FiledHandler），这样日志会被存储在指定的文件中
    filename="logging_info",
    # filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”
    filemode="at",
    # format：指定handler使用的日志显示格式
    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
    # datefmt：指定日期时间格式。
    datefmt="%Y-%m-%d %H:%M:%S %p",
    # level：设置rootlogger 的日志级别
    level=10
)

# 生成器
logger1 = logging.getLogger("日志对象1")

# 文件句柄
handler1 = logging.FileHandler("logging_info", encoding="utf-8")
handler2 = logging.FileHandler("logging_info", encoding="utf-8")

# 控制台句柄,处理器
handler3 = logging.StreamHandler()

# 格式化对象
fmt1 = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s:  %(message)s",
    datefmt="%m-%d %H:%M:%S %p")
fmt2 = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s :  %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S")

# 绑定格式化对象与文件句柄,设置处理器的日志输出格式
handler1.setFormatter(fmt1)
handler2.setFormatter(fmt2)
handler3.setFormatter(fmt1)

# 绑定生成器与文件句柄，添加到处理器中
logger1.addHandler(handler1)
logger1.addHandler(handler2)
logger1.addHandler(handler3)

# 设置日志级别
logger1.setLevel(10)    # 生成器日志级别
handler1.setLevel(20)   # 句柄日志级别

# 测试
logger1.debug("debug msessage")
logger1.info("info msessage")
logger1.warning("warning msessage")
logger1.critical("critical msessage")"""

# 默认情况logging模块输出格式
# logging.warning('%s before you %s', 'look', 'loop')
# logging.handlers.RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]]) -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
# maxBytes用于指定日志文件的最大文件大小。
# backupCount用于指定保留的备份文件的个数。
