# Generated by Django 4.0.6 on 2022-07-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_details', '0003_remove_product_supplied_by'),
        ('userlist', '0010_company_phone_company_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_supplied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_details.product')),
                ('supplied_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.supplier')),
                ('supplied_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userlist.company')),
            ],
        ),
    ]