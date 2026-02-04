# 4.编写一个函数 binary_file_search(filepath, keyword)，接收一个二进制文件路径和一个字节串 keyword。
# 函数在文件中搜索 keyword 首次出现的位置，返回其起始字节位置（从0开始），若未找到返回 -1。
# 要求使用 seek() 和 read()，不能一次性读取整个文件。

def binary_file_search(filepath, keyword):
    """
    简化版本：不考虑关键词跨块的情况

    适用于大多数实际场景，如果关键词可能跨块边界，这个版本可能会漏掉匹配
    """
    if not keyword:
        return 0
    keyword_len = len(keyword)
    with open(filepath, "rb") as f:
        # 创建缓冲区，每次读取固定大小
        buffer_size = 4096
        buffer = b''
        position = 0
        while True:
            # 读取新数据
            chunk = f.read(buffer_size)
            if not chunk:
                break
                # 添加到缓冲区
            buffer += chunk
            # 在缓冲区中搜索关键词
            index = buffer.find(keyword)
            if index != -1:
                return position + index
            # 保留缓冲区末尾的关键词长度-1个字节，防止跨块匹配
            if len(buffer) > keyword_len:
                buffer = buffer[-(keyword_len - 1):] if keyword_len > 1 else b''
                position = f.tell() - len(buffer)
    return - 1







