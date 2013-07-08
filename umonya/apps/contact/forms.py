from django import forms


class ContactForm(forms.Form):
    required = "required"
    name = forms.CharField(label="Name", required=True,
                           widget=forms.TextInput(attrs={"class": required, required: ""}))

    email = forms.EmailField(label="Email Address", required=True,
                             widget=forms.TextInput(attrs={"class": required, required: "",
                                                    "type": "email"}))

    text = forms.CharField(label="Talk to us",
                           widget=forms.Textarea(attrs={}))
