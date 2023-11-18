from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    done = models.BooleanField(blank=True)
    task = models.ManyToManyField(Tag, related_name="task")

    class Meta:
        ordering = ["done", "-datetime"]

    def __str__(self):
        return f"{self.datetime} - {self.content}"
