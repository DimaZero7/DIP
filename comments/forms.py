from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Предстовление о форме коментариев"""

    class Meta:
        model = Comment
        fields = ['product', 'comment_author', 'comment_text']
        exclude = ['product']
        widgets = {

            'comment_author': forms.TextInput(attrs={
                'placeholder': 'Ваше имя', 'class': 'None', 'maxlength': '50'}),

            'comment_text': forms.Textarea(attrs={
                'placeholder': 'Текст комментария', 'class': 'None', 'cols': '30', 'rows': '10', 'maxlength': '200'}),
        }
