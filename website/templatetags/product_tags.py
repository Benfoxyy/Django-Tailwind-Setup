from django import template
from ..models import ProductModel

register = template.Library()

@register.inclusion_tag('includes/similar_prod.html', takes_context=True)
def show_similar_products(context, product):
    request = context['request']
    similar_products = ProductModel.objects.filter(
        category__in=product.category.all()
    ).exclude(id=product.id).order_by('-created_date')[:4]
    context.update({
        'similar_products': similar_products,
        'request': request
    })
    return context