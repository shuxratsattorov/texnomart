from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from texnomart.models import Category, Product
from config.settings import DEFAULT_FROM_EMAIL, BASE_DIR
import os
import json


# def post_save_category(sender, instance, created, **kwargs):
#     if created:
#         print(f'Category {instance.category_name} created')
#     else:
#         print(f'Category {instance.category_name} updated')
#
#
# post_save.connect(post_save_category, sender=Category)
#
#
# def pre_delete_category(sender, instance, **kwargs):
#     print(f'Category {instance.category_name} deleted')
#
#
# pre_delete.connect(pre_delete_category, sender=Category)


@receiver(post_save, sender=Product)
def post_save_product(sender, instance, created, **kwargs):
    if created:
        subject = 'Texnomart'
        message = f'Product {instance.product_name} created'
        from_email = DEFAULT_FROM_EMAIL
        to = 'shuhratsattorov2004@gmail.com'   # you email
        send_mail(subject, message, from_email, [to], fail_silently=False)
    else:
        subject = 'Texnomart'
        message = f'Product {instance.product_name} updated'
        from_email = DEFAULT_FROM_EMAIL
        to = 'shuhratsattorov2004@gmail.com'   # you email
        send_mail(subject, message, from_email, [to], fail_silently=False)


@receiver(pre_delete, sender=Product)
def pre_delete_product(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'texnomart/deletes_data', f'product_{instance.id}.json')

    product_data = {
        'id': instance.id,
        'product_name': instance.product_name,
        'description': instance.description,
        'price': instance.price,
        'quantity': instance.quantity,
        'discount': instance.discount,
        'slug': instance.slug
    }

    with open(file_path, 'w') as json_file:
        json.dump(product_data, json_file, indent=4)

    print(f'Product {instance.product_name} deleted')
