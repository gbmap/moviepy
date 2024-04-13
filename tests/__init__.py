
from functools import wraps

from moviepy import config
from pytest import skip

def requires_imagemagick(f):
    @wraps(f)
    def wrapper(**kwargs):
        print(config.IMAGEMAGICK_BINARY)
        if config.IMAGEMAGICK_BINARY == "unset" or config.IMAGEMAGICK_BINARY == "convert":
            raise skip("requires imagemagick")
        return f(**kwargs)
    return wrapper







