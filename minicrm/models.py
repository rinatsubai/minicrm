from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now

class Artist (models.Model):
    Name = models.CharField(max_length=50)
    Created_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return f"{self.Name}"


class Project (models.Model):
   
    STATUS = (
        ("New", "New"),
        ("Demo", "Demo"),
        ("Fixing", "Fixing"),
        ("Recording", "Recording"),
        ("Trackout", "Trackout"),
        ("Ming", "Mixing"),
        ("Finished", "Finished"),
    )
    
    Name = models.CharField(max_length=50,)
    Artist = models.ForeignKey(Artist, on_delete=models.CASCADE, blank=True, null=True,)
    Status = models.CharField(
        max_length=50,
        choices=STATUS,
        default="NE",)
    Price = models.IntegerField(default=18000)
    Prep = models.IntegerField(default=0)
    Prep_done = models.BooleanField(default=False)
    Postp = models.IntegerField(default=0)
    Postp_done = models.BooleanField(default=False)
    Delta = models.IntegerField(default=0)
    Start_date = models.DateField()
    Post_date = models.DateField()
    Deadline = models.DateField()
    # Time = timezone.now() - timedelta(Start_date)
    Comment = models.CharField(max_length=512)
    
    def __str__(self):
        return f"{self.Name}"
    
class PersonalProject (models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    Comment = models.CharField(max_length=512)
    Links = models.CharField(max_length=512)
    Deadline = models.DateField()
    
    def __str__(self):
        return f"{self.Name}"
    
    