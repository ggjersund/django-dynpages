from django.urls import path
from . import views

urlpatterns = [
    path('<path:url>', views.dynpage, name='dynpages.views.dynpage'),
]