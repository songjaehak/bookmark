from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/bookmark/
    #'' 의 기능은 bookmark/ 이하 부분이 없다고 해석가능 --> 북마크앱의 루트페이지 역할
    # 클래스형 뷰이면 .as_view()로 꼭 사용!!!!

    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]