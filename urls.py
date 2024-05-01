from app import admin
from. import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as log_views






urlpatterns = [
    path("", log_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('register/', views.register, name="register"),
    path('home/', views.home, name ="homepage"),
    path('logout/', log_views.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
    path('notification/', views.notification, name="notification"),  
    path('notificationpage/', views.notification_page, name='notificationpage'),
    path('eqiupmentlist', views.equipmentlist, name="equipmentlist"),
    path('searchforeqiupment', views.searchforequipment, name="searchforequipment"),
    path('accounts/profile/', views.profile, name="profile"),
    path('admin/', admin.site.urls),
    path('createinventory', views.CreateInventory, name = "app_createinventory"),
    path('equipment/<int:equipment_id>/', views.equipment_detail, name="equipment_detail"),
    path('search/', views.equipment_search, name='equipment_search'),
    path('equipmentlist/', views.equipmentlist, name='equipmentlist'),
    path('update/<int:device_id>/', views.update_equipment, name="update_equipment"),
    path('deleteitem/<int:device_id>/', views.deleteItem, name="deleteitem"),
    path('createinventory/', views.create_item_view, name='app_createinventory'),
    path('view_rented_equipment/', views.view_rented_equipment, name="view_rented_equipment"),
    path('reservationpage/', views.reservation_page, name='reservationpage'),
    path('save-settings/', views.save_notification_settings, name='save_notification_settings'),
    

]

