from fastapi import FastAPI, UploadFile, File, HTTPException, Query

# from fastapi.responses import FileResponse
# import os
#
# app = FastAPI()
#
# # 固件文件目录
# FIRMWARE_DIR = "./firmware"
# CURRENT_VERSION = "1.0.0"  # 当前固件版本
#
# # 确保固件目录存在
# os.makedirs(FIRMWARE_DIR, exist_ok=True)
#
#
# @app.get("/")
# async def root():
#     return {"message": "Welcome to ESP32-S3 OTA Server!"}
#
#
# @app.get("/ota/update")
# async def ota_update(version: str):
#     """
#     提供OTA更新功能
#     - version: 设备传递的当前版本号
#     """
#     if version == CURRENT_VERSION:
#         return {"message": "Your firmware is up-to-date."}
#
#     firmware_path = os.path.join(FIRMWARE_DIR, "firmware.bin")
#     if os.path.exists(firmware_path):
#         return FileResponse(
#             firmware_path,
#             media_type="application/octet-stream",
#             filename="firmware.bin",
#         )
#     else:
#         raise HTTPException(status_code=404, detail="Firmware not found")
#
#
# @app.post("/ota/upload")
# async def ota_upload(file: UploadFile = File(...)):
#     """
#     上传新的固件文件
#     """
#     if file.filename.endswith(".bin"):
#         file_path = os.path.join(FIRMWARE_DIR, "firmware.bin")
#         with open(file_path, "wb") as f:
#             f.write(await file.read())
#         return {"message": "Firmware uploaded successfully!"}
#     else:
#         raise HTTPException(status_code=400, detail="Invalid file format. Only .bin files are allowed.")
#
#
# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="0.0.0.0", port=5000)
import os

from fastapi import FastAPI
from libs import Init

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to OTA Server!"}


@app.post("/upload")
async def ota_upload(file: UploadFile = File(...), series: str = Query(...)):
    """
    上传新的固件文件
    :param series: 固件系列名称
    :param file: 上传的文件
    :return:
    """
    from libs import WebAPI
    if not os.path.exists("firmware/" + series):
        raise HTTPException(status_code=400, detail="Invalid series name,This series name is not exist.")
    elif not file.filename.endswith(".bin"):
        raise HTTPException(status_code=400, detail="Invalid file format. Only .bin files are allowed.")
    else:
        file_path = os.path.join("firmware/" + series, WebAPI.name_firmware(firmware_info, series))
        with open(file_path, "wb") as f:
            f.write(await file.read())
        return {"message": "Firmware uploaded successfully!"}


if __name__ == "__main__":
    Init.init()
    server_config = Init.init_server_config()
    firmware_info = Init.load_firmware_info()
    firmware_series = Init.init_firmware(firmware_info)

    import uvicorn
    uvicorn.run(app, host=server_config[0], port=server_config[1])
