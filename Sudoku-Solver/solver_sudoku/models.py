from django.db import models

# Create your models here.
class Solutions(models.Model):
    input_sudoku = models.JSONField()
    solution_sudoku = models.JSONField()