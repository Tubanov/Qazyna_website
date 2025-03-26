from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=250)
    content = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=0)
    image = models.ImageField('Фото', upload_to='images/')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/{self.id}'