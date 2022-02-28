import platform
import logging


def windows_only(func):
    return _platform_only(func, "Windows")


def macos_only(func):
    return _platform_only(func, "Darwin")


def linux_only(func):
    return _platform_only(func, "Linux")


def _platform_only(func, platform_name: str):
    def wrapper(*args, **kwargs):
        if platform.system() != platform_name:
            logging.warning(f"{func.__name__} is windows supported only. Skipping..")
            return args[0]  # return self
        return func(*args, **kwargs)

    return wrapper
