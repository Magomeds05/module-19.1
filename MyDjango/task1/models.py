from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField(max_length=3)



class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=1000, decimal_places=2)
    description = models.TextField(max_length=300)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

# Создайте в приложении task1 следующие модели:
# 1.Buyer - модель представляющая покупателя.
# Обладает следующими полями:
# name - имя покупателя(username аккаунта)
# balance - баланс(DecimalField)
# age - возраст.
# 2.Game - модель представляющая игру.
# Обладает следующими полями:
# title - название игры
# cost - цена(DecimalField)
# size - размер файлов игры(DecimalField)
# description - описание(неограниченное кол-во текста)
# age_limited - ограничение возраста 18+ (BooleanField, по умолчанию False)
# buyer - покупатель обладающий игрой (ManyToManyField). У каждого покупателя может быть игра и у каждой игры может быть несколько обладателей.
# DecimalField - поле для дробных чисел.
# BooleanField - поле для булевых значений.
# Создайте миграции этих моделей в базу данных и мигрируйте их.
# В результате должны получится 3 таблицы. Проверьте их с помощью DB Browser:
