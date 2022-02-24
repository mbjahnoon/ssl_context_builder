import platform
import logging

print(platform.system())


def windows_only(func):
    def wrapper(*args, **kwargs):
        if platform.system() != "Windows":
            logging.warning(f"{func.__name__} is windows supported only. Skipping..")
            return args[0]  # return self
        return func(*args, **kwargs)

    return wrapper


def macos_only(func):
    def wrapper(*args, **kwargs):
        if platform.system() != "Darwin":
            logging.warning(f"{func.__name__} is MacOS supported only. Skipping..")
            return args[0]  # return self
        return func(*args, **kwargs)

    return wrapper


def linux_only(func):
    def wrapper(*args, **kwargs):
        if platform.system() != "Linux":
            logging.warning(f"{func.__name__} is Linux supported only. Skipping..")
            return args[0]  # return self
        return func(*args, **kwargs)

    return wrapper
