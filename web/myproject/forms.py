from django import forms 

class UploadFileForm(forms.Form):
    oil_xml_file = forms.FileField()
