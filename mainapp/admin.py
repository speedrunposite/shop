from PIL import Image
from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe
from .models import *

class TileAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображение с минимальным разрешением {}x{} и размером не более 5MB.<br>\
                Изображение с разрешением более {}x{} автоматически сожмется до максимально возможного.</span>'.format(
            *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 5MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        return image


# с помощью такой конструкции мы исключаем лишние категории из выбора при создании продукта
class TileAdmin(admin.ModelAdmin):

    form = TileAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tiles'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class StairAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображение с минимальным разрешением {}x{} и размером не более 5MB.<br>\
                Изображение с разрешением более {}x{} автоматически сожмется до максимально возможного.</span>'.format(
            *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 5MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        return image


class StairAdmin(admin.ModelAdmin):

    form = StairAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='stairs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class PavingSlabAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображение с минимальным разрешением {}x{} и размером не более 5MB.<br>\
                Изображение с разрешением более {}x{} автоматически сожмется до максимально возможного.</span>'.format(
            *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 5MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        return image


class PavingSlabAdmin(admin.ModelAdmin):

    form = PavingSlabAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='paving_slabs'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class OurProjectAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            '<span style="color:red; font-size:14px;">Загружайте изображение с минимальным разрешением {}x{} и размером не более 5MB.<br>\
                Изображение с разрешением более {}x{} автоматически сожмется до максимально возможного.</span>'.format(
            *Product.MIN_RESOLUTION, *Product.MAX_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 5MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        return image


class OurProjectAdmin(admin.ModelAdmin):

    form = OurProjectAdminForm

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Tile, TileAdmin)
admin.site.register(Stair, StairAdmin)
admin.site.register(PavingSlab, PavingSlabAdmin)
admin.site.register(OurProject, OurProjectAdmin)