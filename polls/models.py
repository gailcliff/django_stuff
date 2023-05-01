from django.db import models
from django.utils import timezone
from datetime import date


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    date_published = models.DateTimeField(default=timezone.now)

    def got_published_recently(self):
        """
        Check if this was question was published at most a week ago
        :return: bool of whether it's recent
        """

        now = timezone.now()
        recent_threshold = now - timezone.timedelta(weeks=1)
        return self.date_published >= recent_threshold

    def __str__(self):
        return f"{self.question_text} Published: {self.date_published}"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.RESTRICT)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField('number of votes', default=0)

    def __str__(self):
        return self.choice_text


class Note(models.Model):
    note = models.TextField()
    time = models.CharField(default=timezone.now().strftime("%I:%M %p"), max_length=10)
    date = models.CharField(default=date.today().strftime("%d/%m/%y",), max_length=10)

    def __str__(self):
        return self.note
