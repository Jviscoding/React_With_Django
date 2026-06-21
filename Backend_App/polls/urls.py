

from django.urls import path
from .views import ProductListCreateAPIView, ProductDetailAPIView, detail, index, results, vote


from django.urls import path


app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path("", index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/",detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", vote, name="vote"),
    path("products/", ProductListCreateAPIView.as_view()),
    path("products/<int:pk>/", ProductDetailAPIView.as_view()),
]