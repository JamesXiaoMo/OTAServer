# 上传固件
import os


def name_firmware(firmware_info: list[dict], firmware_name: str) -> str:
    firmware_status = None
    for i in firmware_info:
        if i["name"] == firmware_name:
            firmware_status = i["status"]
    if firmware_status == "develop":
        for j in os.listdir("firmware/" + firmware_name):
            print(j)
            os.remove(os.path.join("firmware", j))
        return "firmware"
    elif firmware_status == "release":
        print("Have not finished yet.")