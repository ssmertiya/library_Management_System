from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import AdminSignupView, BookListCreateView, BookRetrieveUpdateDeleteView, PublicBookListView

urlpatterns = [
    path('admin/signup/', AdminSignupView.as_view(), name='admin-signup'),
    path('admin/login/', TokenObtainPairView.as_view(), name='admin-login'), #for login and token generation
    path('admin/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'), #for token refresh if access token expire.
    
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
    path('public/books/', PublicBookListView.as_view(), name='public-book-list'),
]

