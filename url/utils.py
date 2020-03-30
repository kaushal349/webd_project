import random
import string
from .models import Url

def code_generator(length = 6, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))

def create_shortcode(length = 6):
    new_code = code_generator(length=length)
    code_exists = Url.objects.filter(shortcode = new_code)
    if code_exists:
        return create_shortcode(length=length)
    return new_code
