from django.db import models
from django.conf import settings
from pages.choices import location_choices
from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=None, editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def categories_count(self):
        return self.venue_categories.all().count()+500

    def categories_count_listings(self):
        return self.venue_categories.filter(is_published=True).count()+500




class Venue(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='venue_categories')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=350)
    postcode = models.CharField(max_length=10)
    location = models.CharField(max_length=100,
                                blank=False,
                                default=None,
                                choices=location_choices)
    alternate_location = models.CharField(max_length=200, blank=True)
    cost = models.FloatField()
    contact = models.CharField(blank=True, max_length=100)
    contact_mobile = models.CharField(max_length=15, blank=True)
    contact_email = models.CharField(max_length=255, blank=True)
    mirrors = models.BooleanField(default=False)
    wooden_floor = models.BooleanField(default=False)
    music_system = models.BooleanField(default=False)
    floor_type = models.CharField(max_length=255, blank=True)
    size = models.CharField(max_length=9, blank=True)
    about_venue = models.TextField(blank=True, max_length=1000)
    notes = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    is_allowed = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    venue_image = models.ImageField(upload_to='venue_image/%Y/%m/%d', default='dance_class.jpg')
    venue_image_1 = models.ImageField(upload_to='venue_image/%Y/%m/%d', blank=True, null=True)
    venue_image_2 = models.ImageField(upload_to='venue_image/%Y/%m/%d', blank=True)
    slug = models.SlugField(default=None, editable=False)

    def __str__(self):
        return f'{self.id}-{self.name} by {self.author}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.author)
        super(Venue, self).save(*args, **kwargs)

    def updated_info(self):
        if self.updated is None:
            return self.timestamp
        return self.updated

    def mirrors_results(self):
        if self.mirrors == True:
            return ('Has Mirrors')
        else:
            return ('No Mirrors')

    def musicsystem_results(self):
        if self.music_system == True:
            return ('Has Music Sytem')
        else:
            return ('No Music System')


    class Meta:
        ordering = ['-id']







