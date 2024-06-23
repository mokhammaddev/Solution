from django.contrib import admin
from main.models import *

admin.site.register(Science)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)


# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'author', 'question')
#
