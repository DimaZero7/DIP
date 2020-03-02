from .models import Comment
from django import forms

# **********************************
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('autor_name', 'comment_text',)