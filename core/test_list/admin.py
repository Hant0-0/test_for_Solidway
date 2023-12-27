from django.contrib import admin

from test_list.models import Dogs


class DogsAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed']
    list_filter = ['breed']


admin.site.register(Dogs, DogsAdmin)
