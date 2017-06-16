from django.db import models


# Create your models here.
class CountSHA(models.Model):
    key = models.CharField(max_length=255, unique=True)
    value = models.FloatField(unique=False)

    def __str__(self):
        return "SHA256: " + self.key + "     Value: " + str(self.value)

    @classmethod
    def create(cls, key, value):
        obj = cls(key=key, value=value)
        return obj
