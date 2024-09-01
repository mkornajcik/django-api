from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api.views import *

router = DefaultRouter()
router.register("stream", StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("", include(router.urls)),
    path("list/", WatchListAV.as_view(), name="movie-list"),
    path("list2/", WatchListGV.as_view(), name="watch-list"),
    path("<int:pk>/", WatchDetailAV.as_view(), name="movie-detail"),
    path("<int:pk>/reviews/create/", ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),
    path("user-reviews/", UserReview.as_view(), name="user-review-detail"),
]
