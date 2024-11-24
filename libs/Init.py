import os


def init_server_config() -> list[str | int]:
    """
    初始化服务器信息
    :return: 服务器地址 端口
    """
    server_config = []
    with open('config.json', 'r', encoding='utf-8') as f:
        import json
        server_config_json = json.loads(f.read())
        server_config.append(str(server_config_json["IP_Addr"]))
        server_config.append(int(server_config_json["Port"]))
    return server_config


def if_project_complete() -> None:
    """
    检查项目文件的完整性
    :return: None
    """
    import os
    if not os.path.exists('firmware'):
        raise Exception('储存固件的文件夹不存在，必须在根目录创建firmware文件夹')
    if not os.path.exists('firmware/Firmware_Info.json'):
        raise Exception('储存固件信息的文件不存在，必须在firmware目录创建Firmware_Info.json文件')
    if not os.path.exists('config.json'):
        raise Exception('服务器配置信息文件不存在，必须在根目录创建config文件')


def load_firmware_info() -> list[dict]:
    """
    加载固件信息文件
    :return: 包含固件信息的列表
    """
    import json
    with open('firmware/Firmware_Info.json', 'r', encoding='utf-8') as f:
        firmware_info = json.loads(f.read())
    return firmware_info['Models']


def init_firmware(firmware_info: list[dict]) -> list[str]:
    """
    初始化固件
    :param firmware_info: 固件信息列表
    :return: 固件列表
    """
    firmware = []
    for i in firmware_info:
        firmware.append(i["name"])
        if not os.path.exists('firmware/' + i["name"]):
            os.mkdir('firmware/' + i["name"])
    return firmware


def init():
    """
    初始化程序
    :return: None
    """
    if_project_complete()
