from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


# Create your models here.
class BlogIndexPage(Page):
  intro = RichTextField(blank=True)

  content_panels = Page.content_panels + [
    FieldPanel('intro', classname="full")
  ]

class BlogPage(Page):
  date = models.DateField("Post date")
  banner_image = models.ImageField(upload_to="blogbanners", blank=True)
  intro = models.CharField(max_length=250)
  body = RichTextField(blank=True)

  search_fields = Page.search_fields + [
    index.SearchField('intro'),
    index.SearchField('title'),
    index.SearchField('body'),
  ]

  content_panels = Page.content_panels + [
    FieldPanel('date'),
    FieldPanel('banner_image'),    
    FieldPanel('intro'),
    FieldPanel('body', classname="full"),
    InlinePanel('gallery_images', label="Gallery Images"),
  ]

class BlogPageGalleryImage(Orderable):
  page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="gallery_images")
  image = models.ForeignKey(
    'wagtailimages.Image', on_delete=models.CASCADE, related_name="+"
  )
  caption = models.CharField(blank=True, max_length=250)

  panels = [
    ImageChooserPanel('image'),
    FieldPanel('caption')
  ]