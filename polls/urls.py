from django import urls
from . import views

urlpatterns = [
    urls.path('', views.home, name='home'),
    # urls.path('<int:question_id>', views.get_question, name='get_question'),
    urls.path('cliffnotes', views.cliffnotes, name='cliffnotes'),
    urls.path('fuud', views.fuud, name='fuud'),
    urls.path('foo/<int:limit>', views.foo, name='foo'),
]
