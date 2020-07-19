"""Books forms."""

# Django
from django import forms


class ContactForm(forms.Form):
    """Contact form."""

    subject = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        """Clean data form."""

        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError('A minimum of 4 words are required')
        return message
