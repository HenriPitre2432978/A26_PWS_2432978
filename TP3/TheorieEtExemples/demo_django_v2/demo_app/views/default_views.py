from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):
    template_name = "demo_app/index.html"

    def get(self, request):
        return render(request, self.template_name)

