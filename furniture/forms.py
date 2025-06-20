from django import forms
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title_ar', 'title_en', 'content_ar', 'content_en']


from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # remove 'role'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'member'  # always assign 'member' role on form submission
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('اسم المستخدم / Username'))
    password = forms.CharField(widget=forms.PasswordInput, label=_('كلمة المرور / Password'))




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'اكتب تعليقك هنا...',
                'class': 'form-control'
            }),
        }