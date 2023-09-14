from pypulse.View import view
from pypulse.Template import RenderTemplate
from baseapp.domain import User


@view(name='hacker', path_trigger='/hacker')
def hacker(request):
    user = User(type='Hacker')
    return RenderTemplate('home.html', {'user_type': user.type, 'path': '/'})
