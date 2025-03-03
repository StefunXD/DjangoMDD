from django.db import models
# Create your models here.


class BlindtestQuestionModel(models.Model):
    correct_answer = models.CharField(max_length=255)
    genre = models.JSONField()
    choices = models.JSONField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return ', '.join(f"{key}: {value}" for key, value in self.__dict__.items() if key != '_state')

    def __repr__(self):
        return self.__str__()


# class GeneralQuestion(BlindtestQuestionModel):
#     pass

# class GenreQuestion(BlindtestQuestionModel):
#     pass

# class ArtistQuestion(BlindtestQuestionModel):
#     pass



# class AbstractBlindTestQuestion(ABC):   
#     def __init__(self, question_type, correct_answer: str, choices: list):
#         self.question_type = question_type
#         self.correct_answer = correct_answer
#         self.choices = choices
    
#     @abstractmethod
#     def question_ask(self):
#         pass

# #SI la question est général
# class GeneralQuestion(AbstractBlindTestQuestion):
#         def question_ask(self):   
#             return {
#                 'type': 'GENERAL',
#                 'correct_answer': self.correct_answer,
#                 'choices': self.choices
#                 }

# class GenreQuestion(AbstractBlindTestQuestion):
#     def question_ask(self):
#         return {
#             'type': 'GENRE',
#             'correct_answer': self.correct_answer,
#             'choices': self.choices
#         }
    
# class GenreArtist(AbstractBlindTestQuestion):
#     def question_ask(self):
#         return {
#             'type': 'ARTISTE',
#             'correct_answer': self.correct_answer,
#             'choices': self.choices
#         }