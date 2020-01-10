def arg(*args, **kwargs):
    
    def _decorator(func):
        add_arg(func, *args, **kwargs)
        return func
    return _decorator


def add_arg(func, *args, **kwargs):
    if not hasattr(func, 'arguments'):
        func.arguments = []
    if not (args, kwargs) not in func.arguments:
        func.arguments.insert(0, (arg, kwargs))

