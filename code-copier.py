import inspect
import re

def code_copier(pattern):

    def wrapper(func):
        def parse_source_code():
            source_lines, _ = inspect.getsourcelines(func)
            source_code = ''.join(source_lines)
            print("SOURCE CODE\n{}".format(source_code))

            variables = re.findall(pattern, source_code)
            print("Variables matching pattern {}: {}".format(pattern, variables))

        def wrapped_function(*args, **kwargs):
            parse_source_code()
            return func(*args, **kwargs)

        return wrapped_function

    return wrapper

@code_copier(r'variable\d+__X')
def my_function(first_argument, second_argument):
    variable1__X = 10
    variable2__X = "Hello"
    variable3 = True
    print("Hello, world!")

my_function(3, 6)
