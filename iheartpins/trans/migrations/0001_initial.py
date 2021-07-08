# Generated by Django 3.2.4 on 2021-06-24 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_sale', models.BooleanField()),
                ('for_trade', models.BooleanField()),
                ('qty_available', models.IntegerField(default=1, verbose_name='quantity available')),
                ('condition', models.CharField(max_length=30)),
                ('descrip', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_listing_created', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('is_inactive', models.BooleanField(default=False)),
                ('pinventory_content', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='listing', to='main.pinventorycontent')),
            ],
        ),
        migrations.CreateModel(
            name='ListingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='None')),
                ('is_primary', models.BooleanField(default=True)),
                ('date_image_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='trans.listing')),
            ],
        ),
    ]
