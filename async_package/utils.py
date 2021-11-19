

def get_timeout(size: int):
    """根据阀值大小，获取超时时间"""
    if 0 <= size < 1e2:
        timeout = 3e1
    elif 1e2 < size < 5e2:
        timeout = 6e1
    else:
        timeout = 6e1 * 2
    return timeout
