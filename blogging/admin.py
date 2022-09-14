from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.
'''
https://docs.djangoproject.com/en/2.1/ref/contrib/admin/
You can’t use this decorator if you have to reference your model admin class in
its __init__() method, e.g. super(PersonAdmin, self).__init__(*args, **kwargs). 
You can use super().__init__(*args, **kwargs).
'''
class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post, Category) #use of decorator option; site points to custom admin site
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine]
    exclude = ('posts',)
    



