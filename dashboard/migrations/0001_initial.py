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
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_item_id', models.CharField(max_length=50, verbose_name='Id do item')),
                ('social_item_text', models.TextField(verbose_name='Texto')),
                ('social_user_id', models.CharField(max_length=50, verbose_name='Id do usuário')),
                ('social_user_screen_name', models.CharField(max_length=50, verbose_name='Nome de usuário')),
                ('social_user_name', models.CharField(max_length=100, verbose_name='Nome')),
                ('social_user_avatar', models.URLField(max_length=250, verbose_name='Avatar do usuário')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='SocialSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_type', models.CharField(choices=[('twitter-search', 'Twitter - Busca')], db_index=True, max_length=30, verbose_name='Tipo de pesquisa')),
                ('search_term', models.CharField(max_length=250, verbose_name='Termo de pesquisa')),
                ('last_collection_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Data da última coleta')),
                ('item_count', models.PositiveIntegerField(default=0, editable=False, verbose_name='Quantidade de itens')),
                ('since_id', models.BigIntegerField(default=0, editable=False, verbose_name='Since id')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('social_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_searchs', to='accounts.SocialAccount', verbose_name='Conta social')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_searchs', to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Busca social',
                'verbose_name_plural': 'Buscas sociais',
            },
        ),
        migrations.AddField(
            model_name='item',
            name='social_search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='dashboard.SocialSearch', verbose_name='Busca social'),
        ),
    ]