# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Comment(models.Model):
    """docstring for Comment"""
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    comment = models.TextField()
    question_id = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} : {}'.format(self.name, self.date_created)


class Question(models.Model):
    """docstring for Comment"""
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    question = models.CharField(max_length=40)
    question_description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} : {}'.format(self.name, self.question)
