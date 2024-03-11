from django.forms import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from main import models
from main.forms import ReservationForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = models.Event.objects.filter(visible=True)
        context['authors'] = models.Author.objects.all()
        context['carousel'] = models.IndexCarousel.objects.all()
        return context


class EventDetailView(DetailView):
    template_name = 'event.html'
    model = models.Event
    slug_field = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        return context


class EventListView(ListView):
    template_name = 'events.html'
    queryset = models.Event.objects.filter(visible=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('sale', None) == '1':
            context['object_list'] = models.Event.objects.filter(sale=True)
        if self.request.GET.get('type', None):
            context['object_list'] = models.Event.objects.filter(category__id=self.request.GET['type'])
        return context


class AboutUsView(ListView):
    template_name = 'about_us.html'
    model = models.AboutUs


class ReservationCreateView(CreateView):
    template_name = 'reservation.html'
    model = models.Client
    fields = ('name', 'email', 'phone', 'comment', 'event',)
    success_url = reverse_lazy('index')

