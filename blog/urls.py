from django.urls import path
from .feeds import LatestPostsFeed
from  .views import (PostListView,
					 post_list_view,
					 post_detail_view,
					 post_share,
					 post_search_view)





app_name='blog'

urlpatterns = [
	#path('', PostListView.as_view(), name='post_list'),
	
	path('', post_list_view, name='post_list'),

	path('tag/<slug:tag_slug>/',
 		 post_list_view, name='post_list_by_tag'),

	path('<int:year>/<int:month>/<int:day>/<slug:post>/',
		 post_detail_view,
		 name='post_detail'),

	path('<int:post_id>/share/', post_share, name='post_share'),

	path('feed/', LatestPostsFeed(), name='post_feed'),

	path('search/', post_search_view, name='post_search'),
]