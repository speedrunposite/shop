from django.contrib import admin
from django.forms import ModelChoiceField
from .models import *

# с помощью такой конструкции мы исключаем лишние категории из выбора при создании продукта
class TileAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='tiles'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Tile, TileAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)