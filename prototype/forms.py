from django import forms

class CSV_Form(forms.Form):
    csv_file = forms.FileField()
