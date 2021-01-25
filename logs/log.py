import logging.handlers
import config
import colorlog

log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}


# 日志配置
# 注意：日志模块暂时不支持多进程
class Logger(logging.Logger):
    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        # 日志文件名
        if filename is None:
            # 从配置文件获取日志文件地址
            file_path = config.log["filePath"]
            filename = file_path
        self.filename = filename

        # 创建一个handler，用于写入日志文件 ('midnight'：每天凌晨分割生产新的日志文件)
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, when='midnight')
        # fh = logging.handlers.WatchedFileHandler(self.filename)
        #fh.suffix = "%Y%m%d-%H%M.log"
        #fh.suffix = ".%Y-%m-%d.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义日志文件的输出格式
        fh_formatter = logging.Formatter('[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s')
        fh.setFormatter(fh_formatter)
        # 定义控制台的输出格式（带颜色格式）
        ch_formatter = colorlog.ColoredFormatter(
            fmt='%(log_color)s[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] - %(message)s',
            log_colors=log_colors_config
        )
        ch.setFormatter(ch_formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)
