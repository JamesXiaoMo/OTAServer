# from fastapi import FastAPI, UploadFile, File, HTTPException
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
from fastapi import FastAPI
from libs import init


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to OTA Server!"}


if __name__ == "__main__":
    init.init()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=110)