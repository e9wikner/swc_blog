from datetime import date
from django.db import models
from django.db.models import permalink


DRAFT = 1
PUBLIC = 2
STATUS_CHOICES = ((DRAFT, "Draft"), (PUBLIC, "Public"),)


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    pub_date = models.DateField(db_index=True, auto_now_add=True)
    mod_date = models.DateField(db_index=True, auto_now_add=True)

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        kwargs = {"year": self.pub_date.year,
                  "month": self.pub_date.month,
                  "day": self.pub_date.day,
                  "slug": self.slug}

        if self.status == DRAFT:
            # return "blog-view-post-draft", None, kwargs
            return "blog-view-post", None, kwargs
        elif self.upcoming:
            # return "blog-view-post-upcoming", None, kwargs
            return "blog-view-post", None, kwargs
        else:
            return "blog-view-post", None, kwargs

    @property
    def upcoming(self):
        return self.pub_date > date.today()
