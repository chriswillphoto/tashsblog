from django.db import models

from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    subheading = models.CharField(max_length=250, blank=True)
    info_heading_1 = models.CharField(max_length=250, blank=True)
    info_box_1 = models.TextField(blank=True)
    info_heading_2 = models.CharField(max_length=250, blank=True)
    info_box_2 = models.TextField(blank=True)
    info_heading_3 = models.CharField(max_length=250, blank=True)
    info_box_3 = models.TextField(blank=True)
    info_heading_4 = models.CharField(max_length=250, blank=True)
    info_box_4 = models.TextField(blank=True)
    intro_about = RichTextField(blank=True)
    intro_about_image = models.ImageField(upload_to="homepage", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('info_heading_1'),
        FieldPanel('info_box_1', classname="full"),
        FieldPanel('info_heading_2'),
        FieldPanel('info_box_2', classname="full"),
        FieldPanel('info_heading_3'),
        FieldPanel('info_box_3', classname="full"),
        FieldPanel('info_heading_4'),
        FieldPanel('info_box_4', classname="full"),
        FieldPanel('intro_about', classname="full"),
        FieldPanel('intro_about_image')

        
    ]

class LandingPage(Page):
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
