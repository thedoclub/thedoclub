import hashlib
import uuid
import random
import datetime
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from oauth.models import GitHubRepo, GitHubUser


class Presentation(models.Model):
    user = models.ForeignKey(GitHubUser, related_name="presentations")
    repo = models.OneToOneField(GitHubRepo, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    is_submitted = models.BooleanField(default=False)
    
    def build_slides(self):
        self.title = self.repo.name
        self.description = self.repo.description
        self.save()
        
        for slide_number in range(5):
            slide_number += 1
            slide, _ = Slide.objects.get_or_create(presentation=self, order=slide_number)
            if not slide.content:
                slide.content = render_to_string('slides/slide%s.md' % slide_number, {
                    "user": self.user,
                    "repo": self.repo,
                    "presentation": self,
                })
                slide.save()
    
    def save_slides(self, slides):
        for s, slide_data in enumerate(slides):
            slide, _ = Slide.objects.get_or_create(presentation=self, order=s+1)
            slide.content = slide_data[0]
            slide.html = slide_data[1]
            slide.save()
        
    def __unicode__(self):
        return "%s: %s" % (self.user, self.repo)


class Slide(models.Model):
    presentation = models.ForeignKey(Presentation, related_name='slides')
    order = models.IntegerField()
    content = models.TextField(null=True, blank=True)
    html = models.TextField(null=True, blank=True)
    
    def __unicode__(self):
        return "%s: Slide #%s (%s bytes)" % (self.presentation, self.order, len(self.content))

