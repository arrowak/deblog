from django.contrib import admin

from polls.models import Choice
# Register your models here.
from polls.models import Question

admin.site.register([Question, Choice])
