from django.views.generic import TemplateView


class TeletestView(TemplateView):
    template_name = "./index.html"
