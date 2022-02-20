# Generated by Django 4.0.2 on 2022-02-18 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleFile', models.CharField(max_length=250, verbose_name='Название файла')),
                ('locsave', models.FileField(upload_to='myapp/static/maketFiles/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Nomenklats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleNome', models.CharField(max_length=250, verbose_name='Название номенклатуры')),
                ('values', models.SmallIntegerField(blank=True, verbose_name='Объем')),
                ('quantity', models.SmallIntegerField(blank=True, verbose_name='Вложение')),
                ('plant', models.CharField(max_length=250, verbose_name='Площадка')),
                ('releases_form', models.CharField(max_length=250, verbose_name='Форма выпуска')),
                ('country', models.CharField(max_length=250, verbose_name='Страна')),
                ('dataNomenlats', models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время')),
                ('infoNome', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Номенклатура',
                'verbose_name_plural': 'Номенклатуры',
            },
        ),
        migrations.CreateModel(
            name='Makets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleMaket', models.CharField(max_length=250, verbose_name='Название')),
                ('typeMaket', models.CharField(max_length=250, verbose_name='Тип макета')),
                ('gregId', models.CharField(max_length=250, verbose_name='Greg-ID')),
                ('infoMaket', models.TextField(verbose_name='Описание')),
                ('dataMaket', models.DateTimeField(auto_now_add=True, verbose_name='Дата/Время')),
                ('imgFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.files')),
            ],
            options={
                'verbose_name': 'Макет',
                'verbose_name_plural': 'Макеты',
            },
        ),
        migrations.CreateModel(
            name='Comm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aktuality', models.BooleanField(verbose_name='Актуальность')),
                ('whoMakets', models.ManyToManyField(blank=True, to='myapp.Makets')),
                ('whoNomenklats', models.ManyToManyField(blank=True, to='myapp.Nomenklats')),
            ],
            options={
                'verbose_name': 'Связи',
                'verbose_name_plural': 'Связи',
                'ordering': ['aktuality'],
            },
        ),
    ]