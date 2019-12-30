from django.urls import path

from .views import (foods, place_order, check_status, cancel_order)

urlpatterns = [
	path('foods/<int:restaurant_id>/', foods),
	path('place-order/', place_order),
	path('check-status/<int:order_id>', check_status),
	path('cancel-order/<int:order_id>', cancel_order)
]