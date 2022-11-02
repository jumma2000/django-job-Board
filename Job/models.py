from django.db import models

# Create your models here.

JOB_TYPE = [
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
]
class Job(models.Model):
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20,choices = JOB_TYPE, blank=True, null=True)
    descripion = models.TextField(max_length=800,blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experince = models.IntegerField(default=1)
    

    class Meta:
        db_table="job"
        verbose_name="job"
        verbose_name_plural="jobs"
    
    def __srt__(self):
        return self.title