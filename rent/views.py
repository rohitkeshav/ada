import os

from ada_project import settings

from django.views.generic import View
from django.http import HttpResponse


class ServeReactApp(View):
    def get(self, request):
        try:
            with open(os.path.join(settings.REACT_APP, 'build', 'index.html')) as f:
                return HttpResponse(f.read())
        except FileNotFoundError:
            return HttpResponse(
                """
                This URL is only used when you have built the production
                version of the app. Visit http://localhost:3000/ instead, or
                run `yarn run build` to test the production version.
                """,
                status=501,
            )
