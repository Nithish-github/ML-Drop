from django import forms

class UploadFilesForm(forms.Form):
    images_folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}))  # Use ClearableFileInput
    labels_folder = forms.FileField(widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}))  # Use ClearableFileInput
    classes_file = forms.FileField()
