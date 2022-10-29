from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="Write Your comment....", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text Here !!!', 'rows': '2', 'column': '50'}))

    class Meta:
        model = Comment
        fields = ('content',)