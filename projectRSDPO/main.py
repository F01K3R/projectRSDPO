import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


import pandas as pd
from bdapp.models import Data2018


exel_data = pd.read_excel('C:/Users/666ki/Desktop/YP/DATA/EGE_RESULT/2018_DATA.xlsx')

for index, row in exel_data.iterrows():
    Data2018.objects.create(stud_id=row['ID'], school_code=row['Код школы'], class_number=row['Класс'],
                            subject_code=row['Предмет'], subject_name=row['Название предмета'], first_result=row['Первичный балл'],
                            percent_result=row['Процент выполнения'], hundred_result=row['100 балльная шкала'], first_result_short=row['Первичный балл за часть с кратким ответом'],
                            result_short=row['Оценка кратких ответов'], first_result_long=row['Первичный балл за часть с развернутым ответом'], result_long=row['Оценка развернутых ответов'],
                            first_result_oral=row['Первичный балл за усную часть'], result_oral=row['Оценка устных ответов'])
