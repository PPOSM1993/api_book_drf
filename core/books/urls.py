from django.urls import path
from . import views

from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView


urlpatterns = [
    #List Data API
    path('books/gender/list/', views.GenderBookList.as_view(), name='gender_book_list'),
    path('books/list/', views.BookList.as_view(), name='book_list'),
    #Create Data API
    path('books/gender/create/', views.GenderBookCreate.as_view(), name='gender_create'),
    path('books/create/', views.BookCreate.as_view(), name='book_create'),

    #Update Data API
    path('books/gender/list/<int:pk>/', views.GenderBookDetail.as_view(), name='gender_detail'),
    path('books/list/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),

    path('docs/', include_docs_urls(title="Library API")),
    path('api_schema/', get_schema_view(title='API Todo APP Schema', description='Guide for REST API with Django'), name='api_schema'),
    path('docs_api/', TemplateView.as_view(template_name='docs.html', extra_context={'schema_url':'api_schema'}), name='swagger-ui'),

    
]