from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

from .models import (AnswerOption, AnswerToQuestion, CompletedSurvey, Question,
                     Survey)


class AnswerOptionInline(NestedStackedInline):
    """Класс для отображения вариантов ответа в вопросе"""
    model = AnswerOption
    extra = 1
    fk_name = 'question'


class QuestionInline(NestedStackedInline):
    """Класс для отображения вопросов в опросе"""
    model = Question
    extra = 1
    inlines = [AnswerOptionInline]
    fk_name = 'survey'


class SurveyAdmin(NestedModelAdmin):
    """Класс для администрирования опросов"""
    inlines = [QuestionInline]


class AnswerToQuestionInline(admin.StackedInline):
    """Класс для отображения вопросов и ответов в завершенном опросе"""
    model = AnswerToQuestion
    extra = 0
    min_num = 1
    readonly_fields = ('question', 'answer')
    can_delete = False


class CompletedSurveyAdmin(admin.ModelAdmin):
    """Класс для администрирования опросов"""
    list_display = (
        'survey',
        'user',
    )
    readonly_fields = (
        'survey',
        'user',
    )
    inlines = [AnswerToQuestionInline]
    list_filter = (
        'survey', 'user',
    )


admin.site.register(Survey, SurveyAdmin)
admin.site.register(CompletedSurvey, CompletedSurveyAdmin)
