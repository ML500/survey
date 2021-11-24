from django.contrib import admin

# Register your models here.
from api.models import Survey, Question, Option, Answer

admin.site.register(Survey)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)