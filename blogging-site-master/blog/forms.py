from django import forms
from blog.models import post,comment

class postForm(forms.ModelForm):


    class Meta:
        model=post
        fields=['auther','title','text']

        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class' : 'editable medium-editor-textarea postcontent'}),



        }

class commetForm(forms.ModelForm):

    class Meta:
        model=comment
        fields=['author','text']
        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),



        }
