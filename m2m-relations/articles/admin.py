from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


from .models import Article, Tag, Scope


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_count = 0

        for form in self.forms:
            cleaned_data = form.cleaned_data

            if not cleaned_data:
                continue
            
            if cleaned_data.get('DELETE'):
                continue
            
            if cleaned_data.get('is_main'):
                main_count += 1
        
        if main_count == 0:
            raise ValidationError('Необходимо выбрать основной раздел')
        elif main_count > 1:
            raise ValidationError('Основной раздел может быть только один')
        
        return super().clean()
        

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
