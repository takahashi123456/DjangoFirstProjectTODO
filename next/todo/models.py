from django.db import models

# 優先度のmodel
choice = (("denger","high"),("primary","low"))

class todoModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    dateline = models.DateField(null=True)
    now_date = models.DateField(auto_now=True,null=True)
    priority= models.CharField(
        max_length=50,
        choices=choice
    )

    def __str__(self):
        return self.title