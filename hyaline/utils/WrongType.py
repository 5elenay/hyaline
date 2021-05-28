def raise_error(variable, name, check) -> None:
    if isinstance(check, tuple):
        if not type(variable) in check:
            raise TypeError(
                f"Argument '{name}' type must be {' / '.join([i.__name__ if i != None else 'None' for i in check])}, not {type(variable).__name__}.")
    else:
        if not isinstance(variable, check):
            raise TypeError(
                f"Argument '{name}' type must be {check.__name__ if check != None else 'None'}, not {type(variable).__name__}.")
