"""
ASGI config for jungle_site project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os
#
# from django.core.asgi import get_asgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jungle_site.settings')
#
# application = get_asgi_application()


import os
from django.apps import apps
from django.conf import settings
# from django.core.wsgi import get_wsgi_application
from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jungle_site.settings")
apps.populate(settings.INSTALLED_APPS)


from fastapi import FastAPI
# from fastapi.middleware.wsgi import WSGIMiddleware
from starlette.middleware.cors import CORSMiddleware

from api.endpoints import api_router


def get_application() -> FastAPI:
    app = FastAPI(title='PROJECT_NAME',
                  # debug=settings.DEBUG
                  )
    app.add_middleware(
        CORSMiddleware,
        # allow_origins=settings.ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router, prefix="")
    # app.mount("/", get_asgi_application())

    return app


app = get_application()
