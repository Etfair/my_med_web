from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import CategoryListView, ContactsListView, MedlistView, \
    ServiceDetailView, CommentListView, CommentCreateView, BLogListView, BLogDetailView

urlpatterns = [
    # Category и Service
    path('', CategoryListView.as_view(), name='category_list'),
    path('<int:pk>/', MedlistView.as_view(), name='med_list'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_view'),

    # Contacts
    path('contacts/', ContactsListView.as_view(), name='contacts'),

    # Comments
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('create_comments/', CommentCreateView.as_view(), name='comment_create'),

    # BLog
    path('blog/', BLogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BLogDetailView.as_view(), name='blog_view')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
