from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil  # copy delete read archive

router = APIRouter()

# ensure folder exists
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# static file set-up
router.mount("/files", StaticFiles(directory=UPLOAD_DIR), name="files")


# upload file api
@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not filename:
        raise HTTPException(status_code=400, detail="File not selected")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file ,  buffer)

        return {
            "message": "file uploaded",
            "filename": filename,
            "file_url": f"http://127.0.0.1:8000/files/{filename}",
        }


@router.get("files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="file not found")

    return {
        "file_url": f" http://127.0.0.1:8000/files/{filename}",
    }
