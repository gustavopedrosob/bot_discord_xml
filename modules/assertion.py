def assert_to_boolean(value: str, error_message: str) -> bool:
    from distutils.util import strtobool
    return bool(strtobool(assert_string_in_list(value, error_message, ["false", "true"])))


def assert_to_entire_number(value: str, error_message: str) -> int:
    return int(__assert_string_function(error_message, str.isdigit, value))


def assert_string_in_list(value: str, error_message: str, _list: list) -> str:
    if value in _list:
        return value
    else:
        raise ValueError(error_message)


def __assert_string_function(error_message: str, function, function_args=None):
    def __end(result):
        if result:
            return result
        else:
            raise ValueError(error_message)

    if callable(function):
        if function_args is None:
            return __end(function())
        elif isinstance(function_args, int) or isinstance(function_args, float) or isinstance(function_args, str):
            return __end(function(function_args))
        elif isinstance(function_args, list) or isinstance(function_args, tuple) or isinstance(function_args, set):
            return __end(function(*function_args))
        elif isinstance(function_args, dict):
            return __end(function(**function_args))
        else:
            TypeError()
    else:
        raise TypeError("The \"function\" argument need to be a function or method.")
