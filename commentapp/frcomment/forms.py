from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Enter your name'}))
    email = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Enter your email address'}))
    question_id = forms.CharField(max_length=50, widget=forms.HiddenInput())
    comment = forms.CharField(widget=forms.Textarea())


class QuestionForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Enter your name'}))
    email = forms.CharField(max_length=20, widget=forms.TextInput({'placeholder': 'Enter your email address'}))
    question = forms.CharField(max_length=40, widget=forms.TextInput({'placeholder': 'Enter your question tittle'}))
    question_description = forms.CharField(widget=forms.Textarea())
