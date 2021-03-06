from django.db import models
import django.contrib.auth.models
from django.forms import ModelForm
import userprofile.models

# Create your models here.

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

class UserProfile(userprofile.models.BaseProfile):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    homepage = models.URLField(blank=True)
    
    def __repr__(self):
        return "<UserProfile: %s>" % self.user

    def __unicode__(self):
        return u"%s" % self.user
    
#    @models.permalink
#    def get_absolute_url(self):
#        return ('profiles_profile_detail', (), { 'username': self.user.username })
