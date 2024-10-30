from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")

    image = models.ImageField(upload_to="profile_image/", null=True, blank=True,
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])
                              ])
    about_me = RichTextField(null=True, blank=True)
    rezyume = models.FileField(null=True, blank=True,
                               validators=[
                                   FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])
                               ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Account for {self.user}"

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        db_table = "account"


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    image = models.ImageField(upload_to="project_image/",
                              validators=[
                                  FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])
                              ])
    url = models.URLField(null=True, blank=True)
    url_name = models.CharField(max_length=30, null=True, blank=True)
    caption = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url_name)

    class Meta:
        db_table = "project"
        verbose_name = "Project"
        verbose_name_plural = "Projects"


class Messages(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "message"
        verbose_name = "Message"
        verbose_name_plural = "Messages"
