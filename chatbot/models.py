from django.db import models

# Create your models here.
class Message(models.Model):
  message = models.TextField(max_length=None, null=None)
  sent_at = models.DateTimeField(auto_created=True)