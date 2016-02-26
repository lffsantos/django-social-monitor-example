# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 07:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(choices=[('twitter', 'Twitter')], db_index=True, max_length=20, verbose_name='Site')),
                ('access_token', models.CharField(max_length=100, verbose_name='Access token')),
                ('access_token_secret', models.CharField(max_length=100, verbose_name='Access token secret')),
                ('account_user_id', models.CharField(max_length=50, verbose_name='User id')),
                ('account_screen_name', models.CharField(max_length=50, verbose_name='Screen name')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Conta social',
                'verbose_name_plural': 'Contas sociais',
            },
        ),
    ]