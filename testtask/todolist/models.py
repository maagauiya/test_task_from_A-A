from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Todolist(models.Model):
    status =[ 
        (1, 'later'),
        (2, 'doing'),
        (3, 'done')
    ]
    task_text=models.TextField(max_length=100,blank=False)
    status = models.IntegerField(_("status"), choices=status,blank=False,default=2)
    userid = models.IntegerField(blank=True,null=True)
