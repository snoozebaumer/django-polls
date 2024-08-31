from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline):  # alt option: admin.StackedInline -> less compact
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
        (None, {"fields": ["allow_multiple_choice"]})
    ]
    inlines = [ChoiceInline]

    list_display = ["question_text", "pub_date", "display_most_voted_choice", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

    # not included in tutorial, had this genius idea myself
    def display_most_voted_choice(self, obj):
        most_voted_choice = obj.choice_with_most_votes()
        return most_voted_choice.choice_text if most_voted_choice else "No choices"

    display_most_voted_choice.short_description = 'Choice with Most Votes'


admin.site.register(Question, QuestionAdmin)
