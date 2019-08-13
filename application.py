from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

from sentry_sdk.integrations.pyramid import PyramidIntegration
import sentry_sdk


def hello_world(request):
    return 1/0
    return Response('<h1>Hello world!</h1>')


def test_func(request):
    return Response("<h1>Hi!, this is Paras Jain</h1>")


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('', '/')
        config.add_view(hello_world, route_name='')
        config.add_route('test', '/test')
        config.add_view(test_func, route_name='test')
        sentry_sdk.init(
            dsn="",
            integrations=[PyramidIntegration()]
        )

    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()