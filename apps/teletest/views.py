from django.views.generic import TemplateView
from django.shortcuts import render
import logging

logger = logging.getLogger("django")


class TeletestView(TemplateView):
    template_name = "index.html"

    def post(self, request):
        logger.info("Кнопка нажата")
        return self.get(request)
