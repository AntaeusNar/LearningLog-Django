from django.db import models


# Create your models here.


class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string definition of self"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(Auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """returns the string."""
        return self.text[:50] + "..."
