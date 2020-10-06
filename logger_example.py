import logging

app_logger = logging.getLogger('app_logger')
app_logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
std_formatter = logging.Formatter(
    fmt='{asctime} - {levelname} - {name} - {message}',
    style='{')
console_handler.setFormatter(std_formatter)

app_logger.addHandler(console_handler)

file_handler = logging.FileHandler('debug.log')
file_handler.setFormatter(std_formatter)
app_logger.addHandler(file_handler)
