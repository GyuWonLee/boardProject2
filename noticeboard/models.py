from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


# Create your models here.


class Notice(models.Model):
    title = models.CharField(max_length=100)
    contents = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    writeId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


