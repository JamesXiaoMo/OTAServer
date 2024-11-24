def if_project_complete():
    """
    检查项目文件的完整性
    :return:
    """
    import os
    if not os.path.exists('firmware'):
        raise Exception('储存固件的文件夹不存在，必须在根目录创建firmware文件夹')
    if not os.path.exists('firmware/Firmware_Info.json'):
        raise Exception('储存固件信息的文件不存在，必须在firmware目录创建Firmware_Info.json文件')


def init():
    """
    初始化程序
    :return:
    """
    if_project_complete()