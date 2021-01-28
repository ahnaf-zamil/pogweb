from pogweb import Request, Extension


my_extension = Extension()


@my_extension.endpoint("/extension")
def ok(request: Request):
    return "This is a POG extension"
