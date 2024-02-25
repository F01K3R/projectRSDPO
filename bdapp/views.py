from django.shortcuts import render
import base64
import matplotlib.pyplot as plt
import pandas as pd
from .models import Data2018


def histogram_view(request):
    data = Data2018.objects.values('subject_name', 'hundred_result')
    df = pd.DataFrame.from_records(data)
    plt.figure(figsize=(10, 6))
    plt.bar(df['subject_name'], df['hundred_result'], color='blue')
    plt.xlabel('Предметы')
    plt.ylabel('Баллы (100 балльная шкала)')
    plt.title('Гистограмма результатов по предметам')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt_img = plt_to_base64(plt)
    context = {'plt_img': plt_img}
    return render(request, 'bdapp/histogram.html', context)


def pie_chart_view(request):
    data = Data2018.objects.values('subject_name', 'percent_result')
    df = pd.DataFrame.from_records(data)
    plt.figure(figsize=(8, 8))
    explode = [0.1] * len(df['subject_name'])
    colors = plt.cm.Set3.colors
    plt.pie(df['percent_result'], labels=df['subject_name'], autopct='%1.1f%%', startangle=90, explode=explode,
            colors=colors, wedgeprops=dict(width=0.4), textprops={'fontsize': 12})
    plt.title('Круговая диаграмма процентов выполнения по предметам')
    plt_img = plt_to_base64(plt)
    context = {'plt_img': plt_img}
    return render(request, 'bdapp/pie_chart.html', context)


def score_range_histogram_view(request):
    data = Data2018.objects.values('subject_name', 'hundred_result')
    df = pd.DataFrame.from_records(data)
    score_ranges = [i for i in range(0, 101, 10)]
    plt.figure(figsize=(10, 6))
    plt.hist(df['hundred_result'], bins=score_ranges, edgecolor='black', alpha=0.7)
    plt.xlabel('Баллы (100 бальная шкала)')
    plt.ylabel('Количество студентов')
    plt.title('Распределение баллов студентов в разных диапазонах')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt_img = plt_to_base64(plt)
    context = {'plt_img': plt_img}
    return render(request, 'bdapp/score_range_histogram.html', context)


def plt_to_base64(plt):
    from io import BytesIO
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    return "data:image/png;base64," + base64.b64encode(image_png).decode('utf-8')


def bd_home(request):
    return render(request, 'bdapp/bdapp_home.html')