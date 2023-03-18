from django import forms

from .models import AnswerOption, AnswerToQuestion, CompletedSurvey


class SurveyForm(forms.Form):
    """Форма для отображения вопросов с варинтами ответа"""
    def __init__(self, *args, **kwargs):
        """Функция инициализации, ожидает в объект Survey."""
        self.survey = kwargs.pop('survey')
        self.user = kwargs.pop('user')
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.create_fields()

    def create_fields(self):
        """Создает поля в форме на основе списка вопросов и ответов
        в опросе"""
        for question in self.survey.questions.all():
            ansnwer_options = [(answer.id, answer.text) for answer in question.answer_options.all()]
            field_name = f'question_{question.id}'
            self.fields[field_name] = forms.ChoiceField(
                widget=forms.RadioSelect,
                choices=ansnwer_options,
                required=True
            )
            self.fields[field_name].label = question.text

    def save(self):
        """Сохраняет ответы из формы, выбранные пользователем
        в объект CompletedSurvey"""
        completed_survey = CompletedSurvey(
            survey=self.survey,
            user=self.user,
        )
        completed_survey.save()
        for question in self.survey.questions.all():
            answer_option = AnswerOption.objects.get(
                pk=self.cleaned_data[f'question_{question.id}'],
            )
            AnswerToQuestion.objects.create(
                survey=completed_survey,
                question=question,
                answer=answer_option
            )
        return completed_survey
