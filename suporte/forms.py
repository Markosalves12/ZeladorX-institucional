from django import forms

class Contact(forms.Form):
    def clean_email(self):
        return self.cleaned_data['email'].strip().title()

    def clean_nome(self):
        return self.cleaned_data['nome'].strip().title()

    nome = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Usuario sobrenome"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "example@email.com.br"
            }
        )
    )

    assunto = forms.CharField(
        label="Assunto",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nova funcionalidade"
            }
        )
    )

    Mensagem = forms.CharField(
        label="Mensagem",
        required=True,
        max_length=3000,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

