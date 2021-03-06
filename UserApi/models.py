import time


from django.db import models


# Create your models here.

class UserDetail(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False, unique=True)
    user_type = models.BooleanField(default=False)
    password = models.CharField(max_length=100, null=False)

    def as_json(self):
        return dict(
            name=self.name,
            email=self.email,
            user_type=self.user_type,
            password=self.password)

    def __str__(self):
        return self.email


class CodeDetail(models.Model):
    code = models.CharField(max_length=14, null=False, unique=True)
    count = models.IntegerField(default=0)
    status = models.CharField(max_length=10, default="unused", null=False)

    def as_json(self):
        return dict(
            code=self.code,
            count=self.count,
            status=self.status)

    def __str__(self):
        return self.code

    @staticmethod
    def generate_uniq_code():
        #code = get_random_string(length=14, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        code = time.time() * 100000000
        code=str(code)[8:22].replace('0',A)
        return code
