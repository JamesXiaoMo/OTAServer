# OTA Server for Microcontrollers

This project provides an **OTA (Over-The-Air)** server designed for microcontrollers. It allows seamless firmware updates via HTTP POST requests, ensuring efficient and reliable firmware delivery to IoT devices.

## Features
- **Firmware Upload**: Upload new firmware files to the server for distribution.
- **Version Control**: Handles firmware versions to prevent unnecessary updates.
- **Scalable**: Supports multiple devices with customizable firmware logic.
- **Secure**: Ensures only authorized updates are applied (optional authentication).

---

## Requirements
- **Python Version**: 3.8 or higher
- **Libraries**:
  - `FastAPI`: For building the HTTP server.
  - `uvicorn`: For running the FastAPI application.

Install dependencies using:
```bash
pip install fastapi uvicorn
