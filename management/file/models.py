from django.db import models
from django.core.validators import FileExtensionValidator


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    contact_num = models.CharField(max_length=15, unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class File(models.Model):
    filename = models.CharField(max_length=1000)
    file = models.FileField(
        upload_to="uploads/",
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'docx', 'xlsx', 'csv', 'txt', 'pptx']
        )]
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_files")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    seen_by = models.ManyToManyField(User, through="FileSeen", related_name="seen_files")

    def __str__(self):
        return self.filename


class FileSeen(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seen_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("file", "user")  

    def __str__(self):
        return f"{self.user.username} saw {self.file.filename} at {self.seen_at}"
