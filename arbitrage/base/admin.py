from django.contrib import admin
from django.forms import ModelForm
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget
from .models import Coin, Dex, CoinPair, DexPair, Result, Setting, BotManager, Whitelist, Analytics
from django import forms
from import_export.admin import ImportExportModelAdmin


class BotManagerForm(ModelForm):
    class Meta:
        model = BotManager
        fields = "__all__"
        widgets = {
            # "start_pause": DjangoToggleSwitchWidget(klass="django-toggle-switch-dark-primary"),
            "start_pause": DjangoToggleSwitchWidget(klass="django-toggle-switch-success"),
        }
        get_latest_by = "order_date"


class BotManagerAdmin(admin.ModelAdmin):
    form = BotManagerForm


class ResultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Result._meta.get_fields()]

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}



class WhitelistForm(ModelForm):
    class Meta:
        model = Whitelist
        fields = "__all__"
        widgets = {
            # "start_pause": DjangoToggleSwitchWidget(klass="django-toggle-switch-dark-primary"),
            "start_pause": DjangoToggleSwitchWidget(klass="django-toggle-switch-success"),
        }


class WhitelistAdmin(admin.ModelAdmin):
    form = WhitelistForm
    # list_display = ['file_link', ]


# class CsvImportForm(ModelForm):
#     # upload = forms.FileField()
#     list_display = ('file_link',)
#
#     def file_link(self, obj):
#         print(obj)
#         if obj.upload:
#             return "<a href='%s' download>Download</a>" % (obj.upload.url,)
#         else:
#             return "No attachment"
#
#     file_link.allow_tags = True
#     file_link.short_description = 'File Download'


# class CsvImportAdmin(admin.ModelAdmin):
#     form = CsvImportForm


# admin.site.register(AppModel, AppAdmin)


admin.site.register(Coin)
admin.site.register(Dex)
admin.site.register(CoinPair)
admin.site.register(DexPair)
admin.site.register(Setting)
admin.site.register(Analytics)
# admin.site.register(Whitelist)

admin.site.register(Result, ResultAdmin)
admin.site.register(BotManager, BotManagerAdmin)
admin.site.register(Whitelist, WhitelistAdmin)
