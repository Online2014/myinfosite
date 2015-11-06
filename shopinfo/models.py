from django.db import models

# Create your models here.

class Shopinformation(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=128, null=True, blank=True)
  tel = models.CharField(max_length=64, null=True, blank=True)
  addr = models.CharField(max_length=256, null=True, blank=True)

  def __unicode__(self):
    return u'%s %s %s ;' %(self.name, self.tel, self.addr)
