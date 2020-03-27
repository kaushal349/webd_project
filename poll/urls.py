from django.urls import path
from .views import home_view, create_view, vote_view, results_view

urlpatterns = [
    path('', home_view , name = 'home'),
    path('create',create_view, name = 'create'),
    path('vote/<poll_id>',vote_view, name = 'vote'),
    path('create/<poll_id>',results_view, name = 'results')
]
