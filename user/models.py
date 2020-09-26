import hashlib
import os
import unicodedata

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe


def user_photo_name(instance, filename):
    m = hashlib.md5()
    m.update(unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore'))
    file_extension = os.path.splitext(filename)
    return "{}{}".format(m.hexdigest(), file_extension[1])


class Profile(AbstractUser):
    photo = models.ImageField(blank=True, null=True, upload_to=user_photo_name)

    def image_tag(self):
        return mark_safe('<img src="%s/%s" width="100px" />' % (settings.MEDIA_URL, str(self.photo)))

    image_tag.short_description = 'Zdjęcie'
    image_tag.allow_tags = True

    def __str__(self):
        """Returns string representation as first_name last_name."""
        return '{} {} - {}'.format(self.last_name, self.first_name, self.username)
