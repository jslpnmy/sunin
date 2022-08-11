from django import forms
from pybo.models import Question, Answer, Proposal


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
