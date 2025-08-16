from django.db import models
from django.utils import timezone 
import uuid 
import hashlib
from datetime import datetime,timedelta

# Create your models here.

def hash_password(raw_password : str) -> str:
    return hashlib.sha256(raw_password.encode()).hexdigest()

class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self,raw_password : str):
        self.password = hash_password(raw_password)

    def check_password(self,raw_password : str) -> bool:
        return self.password == hash_password(raw_password)
    
    def __str__(self):
        return self.username 
    

class Token(models.Model):
    key = models.CharField(max_length=40,unique = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="tokens")
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    @staticmethod
    def generate(user,expiry_minutes = 30):
        token = uuid.uuid4().hex 
        return Token.objects.create(
            key = token,
            user = user,
            expires_at = timezone.now() + timedelta(minutes = expiry_minutes),
        )
    
    def is_expired(self):
        return timezone.now() > self.expires_at