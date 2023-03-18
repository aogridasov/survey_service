import csv
from random import randrange

from django.conf import settings
from django.core.management.base import BaseCommand

from surveys.models import AnswerOption, Question, Survey

PATH = str(settings.BASE_DIR) + '/data/gpt_polls.csv'


class Command(BaseCommand):
    help = 'Загружает CSV с тестовыми опросами в БД проекта'

    @staticmethod
    def create_question(survey, row, index):
        """Создает вопрос и варианты ответа из CSV файла"""
        question = Question.objects.create(
            text=row[index],
            survey=survey
        )
        AnswerOption.objects.create(
            text=row[index + 1],
            question=question
        )
        AnswerOption.objects.create(
            text=row[index + 2],
            question=question
        )

    def handle(self, *args, **options):
        self.stdout.write("Заполняю БД...")
        with open(PATH, newline='', encoding='UTF-8') as ingredients:
            reader = csv.reader(ingredients)
            next(reader)
            for row in reader:
                survey = Survey.objects.create(
                    title=row[0],
                    description=row[1],
                    coins_value=randrange(10, 510, 10)
                )
                # Вопрос 1
                self.create_question(survey, row, 2)
                # Вопрос 2
                self.create_question(survey, row, 5)
        self.stdout.write("Готово!")
