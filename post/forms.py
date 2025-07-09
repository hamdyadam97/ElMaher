from django import forms
from django.utils.translation import gettext_lazy as _
from post.models import Comment


class CommentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        queryset=Comment.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment

        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': _('Write Your Comment Here ...'),
                'class': 'form-control'
            }),
        }
        labels = {
            'text': _('Comment'),
        }