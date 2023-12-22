from pypulse.View import view
from pypulse.Template import RenderTemplate


@view(name="index", path_trigger="/")
def index(request):
    return RenderTemplate("index.html")
