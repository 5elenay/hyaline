def convert(keys: dict) -> str:
    return "?" + '&'.join(f'{i}={keys.get(i)}' for i in keys)
