from django import forms

class InputForm(forms.Form):
    passage = forms.CharField(label="", help_text="", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'20'}))

    def save(self):
        data = self.cleaned_data