from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    subheading = models.CharField(max_length=250, blank=True)
    intro_about = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('subheading'),
        FieldPanel('intro_about', classname="full")
    ]

