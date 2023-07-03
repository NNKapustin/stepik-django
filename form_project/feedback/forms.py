from django import forms
from . import models


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        # fields = ['name', 'rating']  # выбираем какие поля отображать и в каком порядке
        fields = '__all__'  # все, порядок отображения как в модели
        # exclude = ['rating']  # показывать все поля, кроме указанных
        labels = {  # задаются ключ - название поля, значение - текст лейбла
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Оценка',
        }
        error_messages = {
            'name': {
                'max_length': 'ой как много символов',
                'min_length': 'ой как мало символов',
                'required': 'Не должно быть пустым'
            },
        }
