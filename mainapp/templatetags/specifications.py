from django import template
from django.utils.safestring import mark_safe

register = template.Library()


TABLE_HEAD = """
                        <table class="table table-bordered">
                            <tbody>
                        """

TABLE_TAIL = """
                            </tbody>
                        </table>
"""
TABLE_CONTENT ="""
                                <tr>
                                    <td>{name}</td>
                                    <td>{value}</td>
                                </tr>
"""

#Словарь с информацией для продуктов  "Название": "имя в бд"
PRODUCT_SPEC = {
    'tile': {
        'Категория': 'category', 
        'Наименование': 'title', 
        'Размер': 'size', 
        'Единица измерения': 'unit', 
        'Толщина': 'width'
    },
    'stair':{
        'Категория': 'category',
        'Наименование': 'title',
        'Единица измерения': 'unit'
    }
}

def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content

#Создаем тег шаблона
@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    return mark_safe(TABLE_HEAD+get_product_spec(product, model_name) + TABLE_TAIL)