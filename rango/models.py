# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username
    
    
class Document(models.Model):
    docfile = models.ImageField(upload_to='profile_images')
    whiskers = models.ImageField(default = "whiskers_images/beard_PNG6268.png")
    #newimage = models.ImageField
    



