import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Questions(models.Model):
    similar_question = models.CharField(max_length=60)
    name_question_user = models.CharField(max_length=20)
    pub_date = models.DateTimeField("Publié le")
      
    def __str__(self):
        return self.similar_question
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Answers(models.Model):
    questions = models.ForeignKey(Questions,on_delete=models.CASCADE)
    similar_answer = models.CharField(max_length=60)
    name_question_user = models.CharField(max_length=20)
    pub_date = models.DateTimeField("Publié le")

    def __str__(self):
        return self.similar_answer
  
