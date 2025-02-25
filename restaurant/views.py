from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from restaurant.forms import (
    DishForm,
    CookYearsOfExperienceCreateForm,
    CookYearsOfExperienceUpdateForm,
    DishTypeSearchForm,
    DishSearchForm,
    CookSearchForm,
)
from restaurant.models import Cook, Dish, DishType


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "restaurant/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_cooks"] = Cook.objects.count()
        context["num_dishes"] = Dish.objects.count()
        context["num_dish_types"] = DishType.objects.count()

        num_visits = self.request.session.get("num_visits", 0)
        self.request.session["num_visits"] = num_visits + 1
        context["num_visits"] = num_visits + 1

        return context


class DishTypeListView(LoginRequiredMixin, ListView):
    model = DishType
    queryset = DishType.objects.order_by("name")
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishListView(LoginRequiredMixin, ListView):
    model = Dish
    queryset = Dish.objects.select_related("dish_type").order_by("id")
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Dish.objects.all()
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class DishDetailView(LoginRequiredMixin, DetailView):
    model = Dish


class CookListView(LoginRequiredMixin, ListView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes")
    paginate_by = 2
    context_object_name = "cook_list"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = CookSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Cook.objects.all()
        form = CookSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class CookDetailView(LoginRequiredMixin, DetailView):
    model = Cook


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish_type-list")
    template_name = "restaurant/dishtype_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish_type-list")
    template_name = "restaurant/dishtype_form.html"


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish_type-list")
    template_name = "restaurant/dishtype_form_confirm_delete.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form.html"


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("restaurant:dish-list")
    template_name = "restaurant/dish_form_confirm_delete.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookYearsOfExperienceCreateForm


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookYearsOfExperienceUpdateForm


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("restaurant:cook-list")


@login_required
def toggle_dish_assign(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    dish = Dish.objects.get(id=pk)

    if dish in cook.dishes.all():
        cook.dishes.remove(dish)
    else:
        cook.dishes.add(dish)

    return HttpResponseRedirect(reverse_lazy("restaurant:dish-detail", args=[pk]))
