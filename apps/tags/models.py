from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.label


class TaggedItem(models.Model):
    # What tag applied to what object
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE, related_name='tagged_items')
    # Type (product, articles, videos, etc.) -> Find the table
    content_type = models.ForeignKey(to=ContentType, on_delete=models.CASCADE)
    # ID -> Find the object/record in the table
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
