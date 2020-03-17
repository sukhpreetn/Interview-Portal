from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from . import views
from django.views.generic.base import TemplateView # new


app_name = 'AIP'

urlpatterns = [
    path('', views.index, name='index'),
    path('pickskill/', views.pickskill, name='pickskill'),
    path('begin/', views.begin, name='begin'),
    path('quiz/', views.quiz, name='quiz'),
    path('quizsimple/', views.quizsimple, name='quizsimple'),
    path('upload/', views.upload, name='upload'),
    path('comment/', views.comment, name='comment'),
    path('question/', views.question, name='question'),
    path('logout/', views.logout, name='logout'),
    path('export/', views.export, name='export'),
    path('debug/', views.debug, name='debug'),
    path('add/', views.add, name='add'),
    path('questionupload/', views.questionupload, name='questionupload'),
    path('scores/', views.scores, name='scores'),
    path('quizzes/', views.quizzes,name='quizzes'),
    path('addquiz/', views.addquiz,name='addquiz'),
    path('addquestion/', views.addquestion, name='addquestion'),
    path('addquestion1/', views.addquestion1, name='addquestion1'),
    path('quizbucket/', views.quizbucket, name='quizbucket'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
