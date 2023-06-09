from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    """问题表单类
    """

    title = forms.CharField(
        max_length = 255,
        label = _('Title'),
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length = 2000,
        label = _('Description'),
        widget = forms.Textarea(attrs={'class': 'form-control'}),
        help_text = _('Write the question\'s description...')
    )

    # Meta 嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准.
    class Meta:
        model = Question
        fields = ['title', 'description']


class AnswerForm(forms.ModelForm):
    """答案表单类
    """

    description = forms.CharField(
        max_length = 2000,
        widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '4'})
    )

    class Meta:
        model = Answer
        fields = ['description']