from django.db import models

# Create your models here.


class testDB(models.Model):
    id = models.IntegerField('id Результата', primary_key=True)
    result = models.CharField('Результат экзамена', max_length=50)

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Data2018(models.Model):
    stud_id = models.CharField('ID Ученика', max_length=50)
    school_code = models.IntegerField('Код школы')
    class_number = models.CharField('Номер класса', max_length=5)
    subject_code = models.IntegerField('Код предмета')
    subject_name = models.CharField('Название предмета', max_length=30)
    first_result = models.IntegerField('Первичный балл')
    percent_result = models.IntegerField('Процент выполнения')
    hundred_result = models.IntegerField('100 бальная шкала')
    first_result_short = models.IntegerField('Первичный балл краткий ответ')
    result_short = models.CharField('Оценка кратких ответов', max_length=30)
    first_result_long = models.IntegerField('Первичный балл развернутый ответ')
    result_long = models.CharField('Оценка развернутых ответов', max_length=50)
    first_result_oral = models.IntegerField('Первичный балл устный ответ')
    result_oral = models.CharField('Оценка устных ответов', max_length=50)

    def __str__(self):
        return self.stud_id

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
