import requests

# 设置 URL 和查询参数
url = "http://192.168.0.108:110/upload"
params = {
    "series": "FionaPhoneTestDevice0"  # 添加查询参数
}

# 指定要上传的文件路径
file_path = "111.bin"  # 替换为实际文件路径

# 打开文件并上传
try:
    with open(file_path, "rb") as file:
        files = {
            "file": (file_path.split("/")[-1], file)  # 定义文件字段名和文件名
        }
        # 发送 POST 请求
        response = requests.post(url, params=params, files=files)

    # 打印响应结果
    print(f"状态码: {response.status_code}")
    print(f"响应内容: {response.text}")
except FileNotFoundError:
    print(f"文件未找到: {file_path}")
except Exception as e:
    print(f"发生错误: {e}")
