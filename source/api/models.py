from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Заголовок')
    describe = models.TextField(max_length=500, verbose_name='Описание')
    start_date = models.DateField(verbose_name='Дата старта')
    end_date = models.DateField(verbose_name='Дата окончания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    class Type:
        text = 'text'
        one_option = 'one_option'
        plural_option = 'plural_option'

        choices = (
            (text, 'text'),
            (one_option, 'one_option'),
            (plural_option, 'plural_option'),
        )

    survey = models.ForeignKey('Survey', related_name='questions', on_delete=models.CASCADE, verbose_name="Опрос")
    text = models.CharField(max_length=500, verbose_name="Текст")
    type = models.CharField(max_length=30, choices=Type.choices, default=Type.text, verbose_name="Тип")

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Option(models.Model):
    question = models.ForeignKey('Question', related_name='options', on_delete=models.CASCADE, verbose_name="Вопрос")
    text = models.CharField(max_length=500, verbose_name='Текст')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Answer(models.Model):
    user = models.IntegerField()
    survey = models.ForeignKey(Survey, related_name='survey_answers', on_delete=models.PROTECT)
    question = models.ForeignKey(Question, related_name='question_answers', on_delete=models.PROTECT)
    option = models.ForeignKey(Option, related_name='option_answers', on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'