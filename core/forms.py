from django import forms

class ConatctForm(forms.Form):
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super(ConatctForm, self).__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'