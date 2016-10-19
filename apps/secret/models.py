from __future__ import unicode_literals
from ..login.models import User
from django.db import models


# Create your models here.
class SecretManager(models.Manager):
    def addSecret(self, form_data):
        text=Secrets.objects.create(text=form_data['secret'], author=User.objects.get(id=form_data['author']))
        return True
    def deleteSecret(self, s_id):
        Secrets.objects.get(id=s_id).delete()
        return True
    def addLike(self, user_id, s_id):
        secret=self.get(id=s_id)
        user=User.objects.get(id=user_id)
        secret.likes.add(user)
        secret.save()
        return True

class Secrets(models.Model):
    text=models.CharField(max_length=100)
    likes=models.ManyToManyField('login.User', related_name="secrets")
    author=models.ForeignKey('login.User', related_name='secret_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=SecretManager()
