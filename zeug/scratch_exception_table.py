class ExceptionTable(object):
    default = (Exception,'')
    table = {
        IndexError: (IndexError,'500'),
        FileNotFoundError: (FileNotFoundError,'404'),
        EnvironmentError: (EnvironmentError,'300'),
        BufferError: (BufferError,'432'),
    }

    def __init__(self, exception):
        self.name, self.value = self.table.get(type(exception), self.default)

def function_test():
    try:
        raise KeyError("error")
    except Exception as e:
        exception = ExceptionTable(e)
        print(exception.name)
        print(exception.value)

if __name__ == "__main__":
    function_test()
