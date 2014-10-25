from django.db import models

# Create your models here.
class VideoModel(models.Model):
#        homework = models.ForeignKey(Homework, related_name="content_homework")
#        student = models.ForeignKey(User, related_name="content_student")
#        grade = models.IntegerField(blank = True, default = -1)
    description = models.CharField(blank = True, max_length = 1000)
    file = models.FileField(upload_to='file/%Y/%m/%d', blank=True,null=True)


