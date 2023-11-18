from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["status", "-datetime"]

    def __str__(self):
        return f"{self.datetime} - {self.content}"
