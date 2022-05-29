from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('books/', views.index, name='index'),
  # book routes
  path('books/<int:book_id>', views.books_details, name='detail'),
  path('books/create/', views.BookCreate.as_view(), name='books_create'),
  path('books/<int:pk>/update', views.BookUpdate.as_view(), name='books_update'),
  path('books/<int:pk>/delete', views.BookDelete.as_view(), name='books_delete'),
  path('books/<int:book_id>/add_reading', views.add_reading, name='add_reading'),
  path('books/<int:book_id>/assoc_accessory/<int:accessory_id>/', views.assoc_accessory, name='assoc_accessory'),
  # accessorys routes
  path('accessorys/', views.AccessoryList.as_view(), name='accessorys_index'),
  path('accessorys/<int:pk>/', views.AccessoryDetail.as_view(), name='accessorys_detail'),
  path('accessorys/create/', views.AccessoryCreate.as_view(), name='accessorys_create'),
  path('accessorys/<int:pk>/update/', views.AccessoryUpdate.as_view(), name='accessorys_update'),
  path('accessorys/<int:pk>/delete/', views.AccessoryDelete.as_view(), name='accessorys_delete'),
  #Auth Route
  path('accounts/signup/', views.signup, name='signup'),
]