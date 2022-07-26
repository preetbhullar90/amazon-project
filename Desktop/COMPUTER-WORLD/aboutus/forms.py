from django import forms

from .models import NewsletterUsers

class NewsletterUserSignUpForm(forms.ModelForm):
    
    class Meta:
        model = NewsletterUsers
        fields = ["email"]
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            return email
            


