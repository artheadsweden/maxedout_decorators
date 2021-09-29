import inspect


def my_func():
    stack = inspect.stack()
    frame, filename, lineno, function, code_context, index = stack[0]
    print('\n'.join([ filename, str(lineno), function]))
    frame, filename, lineno, function, code_context, index = stack[1]
    print('\n'.join([filename, str(lineno), function]))


def main():
    my_func()


if __name__ == '__main__':
    main()
