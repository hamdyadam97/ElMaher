from django.contrib.auth.forms import UserCreationForm
from user.models import User


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