def qmetrykey(key):
    def decorator(func):
        setattr(func, 'testcaseKey', key)
        return func
    return decorator
