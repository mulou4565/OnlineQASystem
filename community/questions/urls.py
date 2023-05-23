from django.urls import include, path

from .views import CreateQuestionView, QuestionDetailView, QuestionListView
from .views import create_answer


app_name = 'questions'    # 指定路由的命名空间

# /questions/ 问题列表页，GET 请求；
# /questions/add/ 提问页面，GET / POST 请求；
# /questions/<int:pk>/ 问题详情页，GET 请求；
# /questions/<int:pk>/add 提交答案按钮，POST 请求。
urlpatterns = [
    path('questions/', 
        include(([
            path('', QuestionListView.as_view(), name='questions_list'),
            path('add/', CreateQuestionView.as_view(), name='create_question'),
            path('<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
            path('<int:pk>/add', create_answer, name='create_answer'),
        ]))
    ),
]