from .decorators import check_owner
from aiohttp import web
from .route import routes

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

CMD_INFO = {}
PLG_INFO = {}
GRP_INFO = {}
BOT_INFO = []
LOADED_CMDS = {}
