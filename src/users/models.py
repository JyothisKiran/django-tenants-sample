from django.contrib.auth.models import AbstractUser
from django.db import models, connection
from customers.models import Client


class User(AbstractUser):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if not self.client_id:
            self.client = Client.objects.get(schema_name=connection.schema_name)  # Example logic to get the default client
        super().save(*args, **kwargs)
