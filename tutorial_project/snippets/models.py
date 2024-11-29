from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]


# Create your models here.
# https://www.django-rest-framework.org/tutorial/1-serialization/ # tutorial link


