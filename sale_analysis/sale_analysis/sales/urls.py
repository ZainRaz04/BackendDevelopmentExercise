# sales/urls.py
from django.urls import path
from .views import TEAM_PERFORMANCE,REP_PERFORMANCE,PERFORMANCE_TRENDS

urlpatterns = [
    path('rep_performance/', REP_PERFORMANCE.as_view(), name='rep_performance'),
    path('team_performance/', TEAM_PERFORMANCE.as_view(), name='team_performance'),
    path('performaance_trends/', PERFORMANCE_TRENDS.as_view(), name='performance_trends'),
    #path('feedback/', PerformanceFeedbackView.as_view(), name='performance_feedback'),
]
