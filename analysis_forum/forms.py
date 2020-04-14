from django.forms import ModelForm
from .models import File_Forms

class FileUploadForm(ModelForm):
    class Meta:
        model = File_Forms
        fields = ["file_name"]
        
    def __init__(self, *args, **kwargs):
        super(FileUploadForm, self).__init__(*args, **kwargs)
        self.fields["file_name"].widget.attrs.update({'class':'btn btn-outline-info', 'style': 'margin-left:30px', 'id':'file_field', 'required':True, 'name':'file_name'})
