from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from .models import *
from PIL import Image

class TileAdminForm(ModelForm):

    MIN_RESOLUTION = (450, 300)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображение с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = self.MIN_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError(
                'Загруженное изображение: {}x{}. Минимально допустимое резрешение: {}x{}'.format(img.height, img.width, *self.MIN_RESOLUTION))
        return image


# с помощью такой конструкции мы исключаем лишние категории из выбора при создании продукта
class TileAdmin(admin.ModelAdmin):

    form = TileAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tiles'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Tile, TileAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)