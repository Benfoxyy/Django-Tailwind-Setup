# Generated by Django 4.2.14 on 2024-12-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_productcategorymodel_productmodel_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='category',
            field=models.IntegerField(choices=[(1, 'آپارتمانی'), (2, 'تزینی'), (3, 'کادویی')], default=1),
        ),
        migrations.DeleteModel(
            name='ProductCategoryModel',
        ),
    ]
