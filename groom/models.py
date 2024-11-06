from django.db import models
import secrets

# Create your models here.


class Guests(models.Model):
    status_choices = (
        ('WFC', 'Waiting for confirmation'),
        ('C', 'Confirmed'),
        ('R', 'Refused')
    )
    guest_name = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=25, null=True, blank=True)
    maximum_companions = models.PositiveIntegerField(default=0)
    token = models.CharField(max_length=25)
    status = models.CharField(max_length=3, choices=status_choices, default='WFC')

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = secrets.token_urlsafe(16)
        super(Guests, self).save(*args, **kwargs)

    @property
    def link_invitation(self):
        return f'http://127.0.0.1:8000/guests/?token={self.token}'
    
    def __str__(self):
        return self.guest_name


class Gifts(models.Model):
    gift_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='gifts')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    significance = models.IntegerField()
    reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(Guests, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.gift_name
    

