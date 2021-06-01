from base64 import b64encode


def open_and_convert(path: str):
    with open(path, "rb") as f:
        img_bytes = f.read()
        encrypt = b64encode(img_bytes).decode()

        return f"data:image/{f.name.split('.')[-1].replace('jpg', 'jpeg')};base64,{encrypt}"


def convert(data: bytes, img_type: str):
    encrypt = b64encode(data).decode()

    return f"data:image/{img_type};base64,{encrypt}"
