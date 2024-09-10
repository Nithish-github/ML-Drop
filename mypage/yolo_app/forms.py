from django import forms

class UploadFilesForm(forms.Form):
    images_folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    labels_folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    classes_file = forms.FileField()
