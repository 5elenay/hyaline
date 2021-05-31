from base64 import b64encode


def open_and_convert(path: str):
    with open(path, "rb") as f:
        bytes = f.read()
        encrypt = b64encode(bytes).decode()

        return f"data:image/{f.name.split('.')[-1].replace('jpg', 'jpeg')};base64,{encrypt}"


def convert(data: bytes, type: str):
    encrypt = b64encode(data).decode()

    return f"data:image/{type};base64,{encrypt}"
