from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Предстовление о форме коментариев"""

    class Meta:
        model = Comment
        fields = ['user', 'comment_text']
        widgets = {
            'user': forms.TextInput(),

            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Текст комментария', 'maxlength': '200'}),
        }