# Generated by Django 4.0.2 on 2022-02-05 20:33

from django.db import migrations, models
import django.db.models.deletion
import petsatgram.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_pet_user_profile_profile_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='files/', validators=[petsatgram.main.validators.validate_file_size], verbose_name='')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main.Pet')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.profile')),
            ],
        ),
    ]