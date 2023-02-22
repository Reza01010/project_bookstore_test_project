from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend', )


class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend', 'user' )
