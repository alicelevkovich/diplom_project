from django import forms
from scientific_blog.models import Lab, Comment, User, ContactInfo


class CreateUser(forms.Form):
    user_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    lab = forms.ModelChoiceField(queryset=Lab.objects.all())


class UserProfile(forms.Form):
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())
    lab = forms.ModelChoiceField(queryset=Lab.objects.all())
    bio = forms.CharField(widget=forms.Textarea)
    avatar = forms.ImageField()
    position = forms.CharField(max_length=128)


class LogInUser(forms.Form):
    user_name = forms.CharField(max_length=255)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput())


class CreatePost(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ('phone_number', 'address')
