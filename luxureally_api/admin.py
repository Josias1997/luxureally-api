from django.contrib import admin
from .models import User, Restaurant, Category, Food, Table, Order, OrderItem
# Register your models here.

admin.site.site_header = 'Application Admin Dashboard'

class UserInline(admin.TabularInline):
    model = User

class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'password')
	list_display_links = ('first_name', 'last_name')
	list_editable = ('email',)
	search_fields = ['first_name', 'last_name', 'email']


admin.site.register(User, UserAdmin)

class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name', 'all_categories', 'all_tables')
	ordering = ['name']
	search_fields = ['name']
	inlines = [
		UserInline,
	]


admin.site.register(Restaurant, RestaurantAdmin)


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'restaurant', 'created_at')
	ordering = ['title']
	search_fields = ['title', 'created_at', 'restaurant']


admin.site.register(Category, CategoryAdmin)


class FoodAdmin(admin.ModelAdmin):
	list_display = ('title', 'price', 'picture', 'is_active', 'category', 'created_at')
	list_editable = ('price', 'picture', 'category')
	ordering = ['title']
	search_fields = ['title', 'price', 'is_active', 'created_at']


admin.site.register(Food, FoodAdmin)


class OrderInline(admin.TabularInline):
	model = Order

class TableAdmin(admin.ModelAdmin):
	list_display = ('number', 'restaurant')
	list_editable = ('restaurant',)
	ordering = ['number']
	search_fields = ['number', 'restaurant']
	inlines = [
		OrderInline
	]

admin.site.register(Table, TableAdmin)


class OrderItemInline(admin.TabularInline):
	model = OrderItem


class OrderAdmin(admin.ModelAdmin):
	list_display = ('table', 'total_price', 'order_details', 'created_at', 'status')
	list_editable = ('status', )
	search_fields = ['foods', 'table', 'status', 'created_at']
	inlines = [
		OrderItemInline
	]


admin.site.register(Order, OrderAdmin)






