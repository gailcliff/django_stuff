from fastapi import FastAPI
# from django.core.asgi import get_asgi_application
# from jungle_site.asgi import application
from polls.models import Note  # replace with the name of your model

app = FastAPI()

# load the Django settings
# django_asgi_app = get_asgi_application()


# define a route that uses the Django ORM
@app.get("/")
async def read_items():
    items = Note.objects.all()
    return {"items": items}

# run the FastAPI app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
