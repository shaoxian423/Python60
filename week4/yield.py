# generator_log_reader.py

def read_large_file(file_path):
    """
    生成器函数，逐行读取大文件。
    每次调用 yield 返回一行，不会一次性把整个文件加载到内存。
    """
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()  # 去掉行尾换行符


# ------------------- 使用示例 -------------------
if __name__ == "__main__":
    log_file = "data/large_log.txt"  # 替换成你的大文件路径

    # 创建生成器
    log_gen = read_large_file(log_file)

    # 逐行处理（模拟日志流）
    for i, log_line in enumerate(log_gen, 1):
        print(f"{i}: {log_line}")

        # 示例：只读取前10行
        if i >= 10:
            break
