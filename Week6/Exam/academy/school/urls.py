from django.urls import path
from .views import CourseDetails, TeacherListView, SchoolFacilityListView, LaboratoryListView

urlpatterns = [
    path('course/<int:course_id>/', CourseDetails.as_view(), name='course-details'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('facilities/', SchoolFacilityListView.as_view(), name='facility-list'),
    path('laboratories/', LaboratoryListView.as_view(), name='laboratory-list'),
]