from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cook, Dish, DishType


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_cooks'] = Cook.objects.count()
        context['num_dishes'] = Dish.objects.count()
        context['num_dish_types'] = DishType.objects.count()

        num_visits = self.request.session.get('num_visits', 0)
        self.request.session['num_visits'] = num_visits + 1
        context['num_visits'] = num_visits + 1

        return context

class DishTypeListView(ListView):
    model = DishType
    queryset = DishType.objects.order_by("name")
    paginate_by = 2
