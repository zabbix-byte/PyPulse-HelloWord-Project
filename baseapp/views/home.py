from pypulse.View import view
from pypulse.Template import RenderTemplate
from baseapp.domain import User


@view(name='home', path_trigger='/')
def home(request):
    user = User(type='Programmer')
    return RenderTemplate('home.html', {'user_type': user.type})
