from django.contrib import admin
from .models import UserModel, BlogModel, CommentModel
# Register your models here.
admin.site.register(UserModel)
# admin.site.register(BlogModel)
admin.site.register(CommentModel)


class BlogModelAdmin(admin.ModelAdmin):
    #เพิ่มฟิลด์
    list_display = ('text', 'created_on')
    readonly_fields = ('created_on',)

admin.site.register(BlogModel, BlogModelAdmin)
