from django.db import models


class Files(models.Model):
    titleFile = models.CharField('Название файла', max_length=250)
    locsave = models.FileField(upload_to="myapp/static/maketFiles/%Y/%m/%d/", storage=None)

    def __str__(self):
        return self.titleFile
    class Meta:
       verbose_name = 'Файл'
       verbose_name_plural = 'Файлы'


class Makets(models.Model):
    titleMaket = models.CharField('Название', max_length=250)
    typeMaket = models.CharField('Тип макета', max_length=250)
    gregId = models.CharField('Greg-ID', max_length=250)
    imgFile = models.ForeignKey(Files, on_delete=models.CASCADE, blank=True)
    infoMaket = models.TextField('Описание', blank=True)
    dataMaket = models.DateTimeField('Дата/Время', auto_now_add=True)

    def __str__(self):
        return self.titleMaket

    class Meta:
       verbose_name = 'Макет'
       verbose_name_plural = 'Макеты'


class Nomenklats(models.Model):
    titleNome = models.CharField('Название номенклатуры', max_length=250)
    values = models.SmallIntegerField('Объем', blank=True)
    quantity = models.SmallIntegerField('Вложение', blank=True)
    plant = models.CharField('Площадка', max_length=250)
    releases_form = models.CharField('Форма выпуска', max_length=250)
    country = models.CharField('Страна', max_length=250)
    dataNomenlats = models.DateTimeField('Дата/Время', auto_now_add=True)
    infoNome = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.titleNome

    class Meta:
       verbose_name = 'Номенклатура'
       verbose_name_plural = 'Номенклатуры'


class Comm(models.Model):
    whoMakets = models.ManyToManyField(Makets, blank=True)
    whoNomenklats = models.ManyToManyField(Nomenklats, blank=True)
    aktuality = models.BooleanField('Актуальность')

    def __str__(self):
       return self.whoMakets

    class Meta:
       ordering = ['aktuality']
       verbose_name = 'Связи'
       verbose_name_plural = 'Связи'


