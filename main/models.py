from django.contrib.auth.models import User
from django.db import models
from account.models import Account


def question_photo_path(instance, filename):
    return f"question/{instance}/{filename}"


def answer_photo_path(instance, filename):
    return f"answer/{instance}/{filename}"


class Science(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Question(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    # title = models.CharField(max_length=221)
    image = models.ImageField(upload_to=question_photo_path)
    context = models.TextField(null=True, blank=True)
    science = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.context:
            return self.context
        return self.author


class Answer(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)  # only admin or support
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to=answer_photo_path)
    context = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.context


class Comment(models.Model):
    author = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     if self.author.user.get_full_name() == '':
    #         return f"{self.author.user.get_full_name()}'s comment"
    #     return f"{self.author.user.username}'s comment"


