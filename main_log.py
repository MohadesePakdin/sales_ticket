import colorlog,logging

from colorlog import LevelFormatter, TTYColoredFormatter, ColoredFormatter

LOG_FORMAT ="%(log_color)s%(levelname)s%(reset)s:%(name)s:%(message)s"
logging.basicConfig(filename= "info.log",
                     level=logging.INFO,
                     format=LOG_FORMAT)
logging.basicConfig(filename= "info.error",
                     level=logging.ERROR,
                     format=LOG_FORMAT)
logging.basicConfig(filename= "info.warning",
                     level=logging.WARNING,
                     format=LOG_FORMAT)
from colorlog.escape_codes import escape_codes, parse_colors

__all__ = ('escape_codes', 'default_log_colors', 'ColoredFormatter',
           'LevelFormatter', 'TTYColoredFormatter')

# The default colors to use for the debug levels
default_log_colors = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

# The default format to use for each style
# default_formats = {
#     '%': '%(log_color)s%(levelname)s:%(name)s:%(message)s',
#     '{': '{log_color}{levelname}:{name}:{message}',
#     '$': '${log_color}${levelname}:${name}:${message}'
# }


