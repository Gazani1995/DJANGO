from django.contrib import messages
from django.utils.translation import ngettext
from django.contrib import admin
from .models import Article, Category
# Register your models here.
# admin header change
admin.site.site_header = 'وبلاگ'
# ---------------------------------
# updated = queryset.update(author = 1)
@admin.action(description='انتشار مقالات انتخاب شده ')
def make_published(modeladmin, request, queryset):
    updated = queryset.update(status = 'P')
    modeladmin.message_user(request, ngettext(
            '%d مقاله منتشر شد',
            '%d مقاله منتشر شدند',
            updated,
        ) % updated, messages.SUCCESS)


@admin.action(description='پیش نویس مقالات انتخاب شده ')
def make_draft(modeladmin, request, queryset):
    updated = queryset.update(status='b')
    modeladmin.message_user(request, ngettext(
        '%d مقاله پیش نویس شد.',
        '%d مقاله پیش نویس شدند.',
        updated,
    ) % updated, messages.SUCCESS)
   

@admin.action(description='انتشار دسته بندی های انتخاب شده')
def make_publishe(modeladmin, request, queryset):
    updated = queryset.update(status = True)
    modeladmin.message_user(request, ngettext(
        '%d دسته بندی منتشر شد',
        '%d دسته بندی منتشر شدند',
        updated,
    ) % updated, messages.SUCCESS)

@admin.action(description='غیرفعال کردن دسته بندی های انتخاب شده')
def make_drafted(modeladmin, request, queryset):
    updated = queryset.update(status = False)
    modeladmin.message_user(request, ngettext(
        '%d دسته بندی غیرفعال شد ',
        '%d دسته بندی غیرفعال شدند',
        updated,
    ) % updated, messages.SUCCESS)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title','slug', "parent",'status')
    list_filter  = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug' :('title',)}
    actions = [make_publishe , make_drafted]

    

admin.site.register(Category,CategoryAdmin)

# admin.site.register(Article)

admin.site.disable_action('delete_selected')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author','title','thumbnail_tag','slug','status','jpublish', 'category_to_str')
    list_filter  = ('publish','status','author')
    search_fields = ('title','description',)
# pishfarz\\
    prepopulated_fields = {'slug' :('title',)}
    ordering = ['status','publish'] 
    actions = [make_published , make_draft]



admin.site.register(Article,ArticleAdmin)