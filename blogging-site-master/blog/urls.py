from django.urls import path
from blog.views import (aboutview,postlistview,postdetailview,postcreateview,postupdateview,postdeleteview,draftlistviews,
                         add_comment_to_post,comment_approve,comment_remove,post_publish)

urlpatterns=[
          path('',postlistview.as_view(),name='post_list'),
          path('about',aboutview.as_view(),name='about'),
          path('post/<int:pk>/',postdetailview.as_view(),name='post_detail'),
          path('post/new',postcreateview.as_view(),name='post_new'),
          path('post/<int:pk>/edit',postupdateview.as_view(),name='post_edit'),
          path('post/<int:pk>/remove',postdeleteview.as_view(),name='post_remove'),
          path('draft/',draftlistviews.as_view(),name='post_draft_list'),
          path('post/<int:pk>/comment/',add_comment_to_post,name='add_comment_to_post'),
          path('post/<int:pk>/approve/',comment_approve,name='comment_approve'),
          path('post/<int:pk>/remove/',comment_remove,name='comment_remove'),
          path('post/<int:pk>/publish/',post_publish,name='post_publish')


]
