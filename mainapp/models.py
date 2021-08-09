import sys
from PIL import Image
from io import BytesIO

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse

User = get_user_model()


#-----Notes-----
    #  "slug"-это способ генерации действительного URL, как правило, с использованием уже полученных данных.
    #  /categories/stone/ - например 'stone' это и есть slug

    # on_delete=models.CASCADE - обрывание всех связей с объектом при удалении
    
    # ManyToManyField - отношение, при котором многие записи в одной таблице связаны со многими в другой. 
    # Классический пример - это отношение между таблицами Товары и Заказы. 
    # Заказ может включать в себя множество товаров, и в то же время один вид товара может входить в разные заказы.

    # blank & null - https://coderoad.ru/8609192/В-чем-разница-между-null-True-и-blank-True-в-Django

    # related_name - переименование поля в коде (как я понял)

    # class Meta: abstract = True означает, что мы не сможем создать миграцию для этой модели, она абстрактная (обобщитель)
    #reverse - Это означает, что вы ссылаетесь на url только по его атрибуту name - если вы хотите изменить сам url или представление, на которое он ссылается, вы можете сделать это, отредактировав только одно место - urls.py

def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})

# чтобы выводить товары на сайте
class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')
            products.extend(model_products)
        return products


class LatestProducts:

    objects = LatestProductsManager()


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    MIN_RESOLUTION = (100, 100)
    MAX_RESOLUTION = (800, 800)
    MAX_IMAGE_SIZE = 5242880

    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height > max_height or img.width > max_width:
            new_img = img.convert('RGB')
            resized_new_img = new_img.resize((500, 500), Image.ANTIALIAS)
            filestream = BytesIO()
            resized_new_img.save(filestream, 'JPEG', quality=90)
            name = '{}.jpeg'.format(*self.image.name.split('.'))
            filestream.seek(0)
            self.image = InMemoryUploadedFile(filestream, 
            'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None)
        super().save(*args, **kwargs)
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Tile(Product):

    size = models.CharField(max_length=255, verbose_name='Размер')
    unit = models.CharField(max_length=255, verbose_name='Единица измерения')
    width = models.CharField(max_length=255, verbose_name='Толщина')


    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Stair(Product):

    unit = models.CharField(max_length=255, verbose_name='Единица измерения')

    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)
        
    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class PavingSlab(Product):

    size = models.CharField(max_length=255, verbose_name='Размер')
    unit = models.CharField(max_length=255, verbose_name='Единица измерения')
    width = models.CharField(max_length=255, verbose_name='Толщина')

    def __str__(self):
        return '{} : {}'.format(self.category.name, self.title)
        
    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class Contact(models.Model):

    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')

    def __str__(self):
        return '{}'.format(self.phone_number)


class OurProject(models.Model):

    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='', verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def save(self, *args, **kwargs):
        image = self.image
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height > max_height or img.width > max_width:
            new_img = img.convert('RGB')
            resized_new_img = new_img.resize((500, 500), Image.ANTIALIAS)
            filestream = BytesIO()
            resized_new_img.save(filestream, 'JPEG', quality=90)
            name = '{}.jpeg'.format(*self.image.name.split('.'))
            filestream.seek(0)
            self.image = InMemoryUploadedFile(filestream, 
            'ImageField', name, 'jpeg/image', sys.getsizeof(filestream), None)
        super().save(*args, **kwargs)
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()