from django.contrib import admin
from .models import Question, Proposal


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class ProposalAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Proposal, ProposalAdmin)
