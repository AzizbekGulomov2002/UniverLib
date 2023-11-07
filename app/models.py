from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    


class Group(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)    
    desc = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name



class Book(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='books')
    def __str__(self):
        return self.name