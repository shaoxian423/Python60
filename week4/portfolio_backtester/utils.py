from datetime import datetime


def today_str():
    """返回今天日期字符串 YYYY-MM-DD"""
    return datetime.today().strftime("%Y-%m-%d")
