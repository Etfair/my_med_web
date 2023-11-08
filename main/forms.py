from django import forms

from main.models import Comment


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CommentForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
