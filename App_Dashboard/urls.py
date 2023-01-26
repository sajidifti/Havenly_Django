from django.urls import path
from App_Dashboard import views

app_name = 'App_Dashboard'

urlpatterns = [
    path('', views.home, name="home"),

    path('designer_info/', views.designer_info, name='designer_info'),
    path('add_designer/', views.add_designer, name='add_designer'),
    path('view_designer/<int:designer_id>/', views.view_designer, name='view_designer'),
    path('edit_designer/<int:designer_id>/', views.edit_designer, name='edit_designer'),
    path('delete_designer/<int:designer_id>/', views.delete_designer, name='delete_designer'),

    path('post/', views.post, name='post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('view_post/<int:post_id>/', views.view_post, name='view_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),


    path('react_post/<int:post_id>/', views.react_post, name='react_post'),

    path('reply/', views.reply, name='reply'),
    path('desginerMessage/', views.desginerMessage, name='desginerMessage'),
    path('messageReply/<int:message_id>', views.designerMessageReply, name='messageReply'),
    path('myMessageList/', views.myMessageList, name='myMessageList'),

    path('contact_us/', views.contactUs, name='contact_us'),
]