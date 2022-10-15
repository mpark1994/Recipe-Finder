from django import forms

class PostForm(forms.Form):
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Subject",
                "id": "subject",
                "class": "form-control"
            }
        ))

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "message",
                "placeholder": "Message",
                "id": "message",
                "class": "form-control",
                "cols": "30",
                "rows": "10"
            }
        ))

class SubscribeForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Submit your E-mail here",
                "name": "email",
                "type": "email"
            }
        ))

class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "type": "email",
                "class": "form-control",
                "id": "email",
                "placeholder": "E-mail"
            }
        ))
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "subject",
                "placeholder": "Subject"
            }
        ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "message",
                "placeholder": "Message",
                "id": "message",
                "class": "form-control",
                "cols": "30",
                "rows": "10"
            }
        ))

class RecipeForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "name": "query",
                "placeholder": "Type Any Keywords"
            }
        ))
    ingredients = forms.CharField(required=False,
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "name": "ingredients",
                "placeholder": "(Optional) Ingredients"
            }
        ))
    CHOICES = (('standard', 'Standard'),('gluten free', 'Gluten Free'),('vegetarian', 'Vegetarian'),('vegan', 'Vegan'),('pescetarian', 'Pescetarian'),('ketogenic', 'Keto'))
    diet = forms.ChoiceField(choices=CHOICES, 
        widget=forms.Select
        )

class SimpleRecipeForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "name": "search",
                "placeholder": "Type Any Keywords"
            }
        ))