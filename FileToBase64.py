import base64


def file_to_base64(file_path, output_txt=None):
    """将文件转换为Base64字符串"""
    with open(file_path, 'rb') as f:
        file_bytes = f.read()

    base64_str = base64.b64encode(file_bytes).decode('utf-8')

    if output_txt:
        with open(output_txt, 'w') as f:
            f.write(base64_str)
        print(f"Base64数据已保存到: {output_txt}")
    else:
        print("Base64字符串:\n")
        print(base64_str)


# 使用示例
if __name__ == "__main__":
    file_path = "your_file"  # 替换为你的文件路径
    output_file = "output.txt"  # 指定输出文本文件（可选）

    file_to_base64(file_path, output_file)
