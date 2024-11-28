from fastapi import FastAPI, UploadFile, File, HTTPException, Query
import os
from fastapi.responses import FileResponse
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


@app.get("/ota")
async def ota_update(series: str = Query(...), version: str = Query(...)):
    """
    提供OTA更新功能
    :param series: 固件系列
    :param version: 固件版本
    :return:
    """
    status = None

    if series not in firmware_series:
        raise HTTPException(status_code=404, detail="Invalid series name,This series is not exist.")

    for i in firmware_info:
        if i['name'] == series:
            status = i['status']
    if status == "Develop":
        firmware_path = os.path.join("firmware", series + "firmware.bin")
        if os.path.exists(firmware_path):
            return FileResponse(
                firmware_path,
                media_type="application/octet-stream",
                filename="firmware.bin",
            )
        else:
            raise HTTPException(status_code=404, detail="Firmware not found")

    elif status == "Release":
        print("release")
    elif status == "Deprecated":
        raise HTTPException(status_code=404, detail="Firmware was deprecated")


if __name__ == "__main__":
    Init.init()
    server_config = Init.init_server_config()
    firmware_info = Init.load_firmware_info()
    firmware_series = Init.init_firmware(firmware_info)

    import uvicorn

    uvicorn.run(app, host=server_config[0], port=server_config[1])
