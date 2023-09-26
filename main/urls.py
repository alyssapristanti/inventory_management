from django.urls import path

from main.views import (add_stock, create_new_product, delete_product,
                        login_user, logout_user, reduce_stock,
                        register_account, show_json, show_json_by_id,
                        show_main, show_xml, show_xml_by_id)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-new-product', create_new_product, name='create_new_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register_account, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_stock/<int:product_id>/', add_stock, name='add_stock'),
    path('reduce_stock/<int:product_id>/', reduce_stock, name='reduce_stock'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
]