from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'
# pages/views.py
class AboutPageView(TemplateView): # new
    template_name = 'about.html'