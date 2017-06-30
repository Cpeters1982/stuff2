from django.conf.urls import url
from.import views

app_name = 'mybook'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addQuote$', views.addQuote, name='addQuote'),
    url(r'^addFavorite$', views.addFavorite, name='addFavorite')

]
