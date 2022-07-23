from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [

    path('', CoursesView.as_view(), name='courses'),
    # path('new-list/', CoursesView2.as_view(), name='courses'),
    path('create/', CreateCourseView.as_view(), name='create-course'),
    path('level/<int:pk>/<slug:slug>/', CourseLevelDetailView.as_view(), name='level_detail'),
    path('style/<int:pk>/<slug:slug>/', CourseStyleDetailView.as_view(), name='style-detail'),
    path('detail/<int:pk>/<slug:slug>/', SingleCourseView.as_view(), name='course-detail'),
    path('update/<int:pk>/<slug:slug>/', UpdateCourseView.as_view(), name='update-course'),
    path('delete/<int:pk>/<slug:slug>/', DeleteCourseView.as_view(), name='delete-course'),
    path('search/', searchCourse, name='search-course'),
    path('create-review/<int:pk>/', CreateCourseReview.as_view(), name='create-review'),
    path('update-review/<int:pk>/', UpdateCourseReview.as_view(), name='update-review'),
    path('delete-review/<int:pk>/', DeleteReviewView.as_view(), name='delete-review'),

]