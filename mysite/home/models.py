from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.images.models import Image
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    call_to_action = models.CharField(max_length=255, blank=True)
    faq = RichTextField(blank=True)
    testimonial_slider = StreamField(
        [
            ("testimonial", blocks.StructBlock([
                ("quote", blocks.TextBlock(required=True)),
                ("author", blocks.CharBlock(required=False)),
                ("photo", ImageChooserBlock(required=False)),
            ])),
        ],
        blank=True,
        use_json_field=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("call_to_action"),
        FieldPanel("faq"),
        FieldPanel("testimonial_slider"),
    ]


class BlogPage(Page):
    blog_name = models.CharField(max_length=255, help_text="Blog title")
    blog_day = models.DateField(help_text="Publication date")
    image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("blog_name"),
        FieldPanel("blog_day"),
        FieldPanel("image"),
        FieldPanel("body"),
    ]
