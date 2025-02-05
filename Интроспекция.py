import inspect


def introspection_info(obj):
    attr =[]
    methods = []
    for i in dir(obj):
        if inspect.isbuiltin(i) or inspect.isfunction(i) or inspect.ismethod(i):
            methods.append(i)
        else:
            attr.append(i)
    return  {"type": type(obj), 'attributes': attr, 'methods': methods, 'module': inspect.getmodule(obj)}

number_info = introspection_info(42)
print(number_info)
