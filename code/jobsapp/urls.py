from django.urls import path, include

from .views import *

app_name = "jobs"

urlpatterns = [
    path('<int:lang_code>/', HomeView.as_view(), name='home'),
    path('favorite', favorite, name='favorite'),
    path('search', SearchView.as_view(), name='search'),
    path('employer/dashboard/', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
    path('employee/', include([
        path('my-applications', EmployeeMyJobsListView.as_view(), name='employee-my-applications'),
        path('favorites', FavoriteListView.as_view(), name='employee-favorites'),
    ])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('<int:lang_code>/jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
]
