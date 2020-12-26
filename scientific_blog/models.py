from django.db import models
from django.contrib.auth.models import User as AuthUser

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Lab(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=255, default=None)
    email = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=128, default=None)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE, null=True, related_name='lab')

    avatar = models.ImageField(upload_to="images/", null=True, blank=True)
    position = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=30, null=True)
    bio = models.TextField(null=True)

    class Meta:
        ordering = ["-user_name"]

    def __str__(self):
        return f'{self.user_name} {self.email}'


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, default='', null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    name = models.CharField(max_length=80, default='', null=True)
    email = models.EmailField(null=True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=64, null=True)
    address = models.CharField(max_length=128, null=True)

    def __str__(self):
        return f'{self.phone_number} {self.address}'
