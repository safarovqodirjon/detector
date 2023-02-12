from django import forms
from .models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)

    document = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
        'multiple': True,
    }), required=True)


SOME = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Filename1'),
    ('green', 'Filename2'),
    ('black', 'Filename3'),
]


class CheckForm(forms.Form):
    def __init__(self, list=None, *args, **kwargs):
        super(CheckForm, self).__init__(*args, **kwargs)
        self.lst = list
        # self.fields["number"] = forms.Mult(choices=list)

    file_name = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES
    )


class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        my_arg = kwargs.pop('my_arg')
        super(DynamicForm, self).__init__(*args, **kwargs)
        for item in my_arg:
            self.fields['test_field_', item] = forms.MultipleChoiceField(required=False,
                                                                         widget=forms.CheckboxSelectMultiple, )
