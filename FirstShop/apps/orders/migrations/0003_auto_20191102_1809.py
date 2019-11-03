# Generated by Django 2.2.4 on 2019-11-02 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_delivery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('car', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order',
            field=models.ManyToManyField(to='orders.Order'),
        ),
    ]
