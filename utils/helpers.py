# FastApi
from fastapi import HTTPException

# utils
import base64


def save_local_document(path, document):
    with open(path, "wb") as f:
        try:
            f.write(document)
        except Exception as ex:
            raise HTTPException(400, "Invalid document encoding")
