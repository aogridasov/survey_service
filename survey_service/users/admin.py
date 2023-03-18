from django.contrib import admin

from users.models import Coins, Upgrades, User


class CoinsInline(admin.StackedInline):
    model = Coins
    extra = 0
    min_num = 1
    max_num = 1
    readonly_fields = ('user',)
    can_delete = False


class UpgradesInline(admin.StackedInline):
    model = Upgrades
    extra = 0
    min_num = 1
    max_num = 1
    readonly_fields = ('user',)
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'get_surveys',
    )
    list_filter = (
        'username',
    )

    inlines = [CoinsInline, UpgradesInline]

    def get_surveys(self, obj):
        return obj.completed_surveys.count()

    get_surveys.short_description = 'Пройденные опросы'


admin.site.register(User, UserAdmin)
