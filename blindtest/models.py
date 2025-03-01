from django.db import models
from abc import ABC, abstractmethod
from .enums import QuestionType

# Create your models here.
class BlindtestQuestion(models.Model):
    blindtest_type = models.CharField(max_length=15)
    blindtest_goodanwser = models.IntegerField(default=1)

    def __str__(self):
        return self.blindtest_type, self.blindtest_goodanwser

class BlindtestAnswer(models.Model):
    blindtest_question = models.ForeignKey(BlindtestQuestion, on_delete=models.CASCADE)
    blindtest_answer1 = models.CharField(max_length=30)
    blindtest_answer2 = models.CharField(max_length=30)
    blindtest_answer3 = models.CharField(max_length=30)
    blindtest_answer4 = models.CharField(max_length=30)
    blindtest_music = models.CharField(max_length=60)

    def __str__(self):
        return self.blindtest_answer1, self.blindtest_answer2, self.blindtest_answer3, self.blindtest_answer4,

class AbstractBlindTestQuestion(ABC):   
    def __init__(self, blindtest_text: str, correct_answer: str, choices: list):
        self.blindtest_text = blindtest_text
        self.correct_answer = correct_answer
        self.choices = choices
    
    @abstractmethod
    def question_ask(self):
        pass
#SI la question est général
class GeneralQuestion(AbstractBlindTestQuestion):
        def question_ask(self):   
            return {
                'type': 'general',
                'question': self.blindtest_text,
                'choices': self.choices
                }

class GenreQuestion(BlindtestQuestion):
    def question_ask(self):
        return {
            'type': 'genre',
            'question': self.question_ask,
            'choices': self.choices
        }
    
class GenreArtist(BlindtestQuestion):
    def question_ask(self):
        return {
            'type': 'artist',
            'question': self.question_ask,
            'choices': self.choices
        }

class BlindtestQuestionModel(models.Model):
    blindtest_text = models.CharField(max_length=255)
    question_type = models.CharField(
        max_length=20,
        choices=[(tag, tag.value) for tag in QuestionType]
    )
    correct_answer = models.CharField(max_length=255)
    choices = models.JSONField()

    def __str__(self):
        return ', '.join(f"{key}: {value}" for key, value in self.__dict__.items() if key != '_state')

    def __repr__(self):
        return self.__str__()