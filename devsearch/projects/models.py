from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True, blank=True)
    demo_link = models.CharField(max_length=500, null=True, blank=True)
    source_link = models.CharField(max_length=500, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(max_length=100, null=True, blank=True)
    vote_ratio = models.IntegerField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000, null=True, blank=True)
    value = models.CharField(max_length=500, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)   

    def __str__(self):
        return self.value   

class Tag(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) 
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
