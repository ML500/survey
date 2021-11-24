from django.urls import path, include

from api.views.answer import AnswerViewSet, GetAswerByUserId
from api.views.option import OptionViewSet
from api.views.question import QuestionViewSet
from api.views.survey import SurveyViewSet, GetActiveSurveyView

urlpatterns = [
    path('survey/', include([
        path('get', SurveyViewSet.as_view({'get': 'list'})),
        path('get/<int:pk>', SurveyViewSet.as_view({'get': 'retrieve'})),
        path('post', SurveyViewSet.as_view({'post': 'create'})),
        path('patch/<int:pk>', SurveyViewSet.as_view({'patch': 'partial_update'})),
        path('delete/<int:pk>', SurveyViewSet.as_view({'delete': 'destroy'})),
        path('get_active', GetActiveSurveyView.as_view()),
    ])),
    path('question/', include([
        path('get', QuestionViewSet.as_view({'get': 'list'})),
        path('get/<int:pk>', QuestionViewSet.as_view({'get': 'retrieve'})),
        path('post', QuestionViewSet.as_view({'post': 'create'})),
        path('patch/<int:pk>', QuestionViewSet.as_view({'patch': 'partial_update'})),
        path('delete/<int:pk>', QuestionViewSet.as_view({'delete': 'destroy'})),
    ])),
    path('option/', include([
        path('get', OptionViewSet.as_view({'get': 'list'})),
        path('get/<int:pk>', OptionViewSet.as_view({'get': 'retrieve'})),
        path('post', OptionViewSet.as_view({'post': 'create'})),
        path('patch/<int:pk>', OptionViewSet.as_view({'patch': 'partial_update'})),
        path('delete/<int:pk>', OptionViewSet.as_view({'delete': 'destroy'})),
    ])),
    path('answer/', include([
        path('get', AnswerViewSet.as_view({'get': 'list'})),
        path('get/<int:pk>', AnswerViewSet.as_view({'get': 'retrieve'})),
        path('get_user_answer/<int:pk>', GetAswerByUserId.as_view()),
        path('post', AnswerViewSet.as_view({'post': 'create'})),
        path('patch/<int:pk>', AnswerViewSet.as_view({'patch': 'partial_update'})),
        path('delete/<int:pk>', AnswerViewSet.as_view({'delete': 'destroy'})),
    ])),
]
