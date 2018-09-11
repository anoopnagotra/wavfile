from django.db import models

# Create your models here.

from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.
class File(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(max_length=250)
    file_media =  models.FileField(upload_to = 'documents/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)


    def __str__(self):
        return self.file_name

    def __unicode__(self):
        return u"%s" % (self.pk)

    class Meta:
        db_table = "file_upload"
