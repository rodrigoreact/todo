from django.contrib import admin
from django.urls import include, path
from app.views import delete, edit, index, searchdata, sortdata, submit, update

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('todoproy.urls')),
    path('',index,name='index'),
    path('submit',submit,name='submit'),
    path('delete/<int:id>',delete,name='delete'),
    path('list',list,name='list'),
    path('sortdata',sortdata,name='sortdata'),
    path('searchdata',searchdata,name='searchdata'),
    path('edit/<int:id>',edit,name='edit'),
    path('update/<int:id>',update,name='update'),
    ]
