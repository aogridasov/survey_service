from django.db import models

from users.models import User


class Survey(models.Model):
    """Модель опроса"""
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey(
        User,
        related_name='created_surveys',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Автор'
    )
    coins_value = models.SmallIntegerField(verbose_name='Награда')

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопроса"""
    survey = models.ForeignKey(
        Survey,
        related_name='questions',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Опрос'
    )
    text = models.TextField(verbose_name='Текст вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class AnswerOption(models.Model):
    """Модель варианта ответа"""
    question = models.ForeignKey(
        Question,
        related_name='answer_options',
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    text = models.TextField(verbose_name='Текст варианта ответа')

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class CompletedSurvey(models.Model):
    """Модель для пройденного опроса,
    ссылается на опрос, прошедшего пользователя и его ответы на вопросы"""
    user = models.ForeignKey(
        User,
        related_name='completed_surveys',
        null=True,
        on_delete=models.SET_NULL

    )
    survey = models.ForeignKey(
        Survey,
        related_name='completed',
        on_delete=models.CASCADE
    )
    answers = models.ManyToManyField(
        AnswerOption,
        through='AnswerToQuestion',
    )

    class Meta:
        verbose_name = 'Завершенный опрос'
        verbose_name_plural = 'Завершенные опросы'

    def __str__(self):
        return f'{self.survey} пройденный {self.user}'


class AnswerToQuestion(models.Model):
    """Модель отображающая выбранный пользователем ответ
    для конкретного вопроса в конкретном опросе"""
    survey = models.ForeignKey(
        CompletedSurvey,
        on_delete=models.CASCADE,
        related_name='user_answers',
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    answer = models.ForeignKey(
        AnswerOption,
        on_delete=models.CASCADE,
        related_name='user_answers'
    )

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'

    def __str__(self):
        return f'{self.question}: {self.answer}'
