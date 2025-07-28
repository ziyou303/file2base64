import base64


def base64_to_file(Base64_str,file_path):

    file_bytes = base64.b64decode(Base64_str.encode('utf-8'))

    # 保存为文件
    with open(file_path, 'wb') as f:
        f.write(file_bytes)
        f.close()

# 使用示例
if __name__ == "__main__":
    file_path = "your_file"  # 替换为你保存的文件路径
    # 示例的base64字符串 (替换为你的实际数据)
    Base64_DATA = "UEsDBBQAAAAIA..."  # 这里放入base64编码的文件内容

    base64_to_file(Base64_DATA, file_path)