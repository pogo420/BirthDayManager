import sys
from typing import Any


def print_error(error_object, is_exit=True):
    """Function of printing error message"""
    error_message = f"Issue: {error_object}"
    print(error_message)
    if is_exit:
        sys.exit(0)
    else:
        pass


def is_null(object_: Any) -> bool:
    if object_ is None:
        return True
    elif object_ == "":
        return True
    else:
        return False

