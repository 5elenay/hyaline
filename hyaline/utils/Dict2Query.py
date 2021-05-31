def convert(keys: dict) -> str:
    if len(keys) == 0:
        return ""

    return "?" + '&'.join(f'{i}={keys.get(i)}' for i in keys)
