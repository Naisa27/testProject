from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Menu(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    sort = models.IntegerField(verbose_name='порядок сортировки', default=1)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu', kwargs={"slug": self.slug})

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['sort', 'name']



class Article(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    menuPoint = TreeForeignKey(Menu, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
