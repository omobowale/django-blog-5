from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title', 'content']
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise forms.ValidationError("Title should be more than 10 characters")
        
        return title
    
    def clean_content(self):
        content = self.cleaned_data['content'] 
        if len(content) < 100:
            raise forms.ValidationError("Content should be more than 100 characters")
        
        return content
            
        
        