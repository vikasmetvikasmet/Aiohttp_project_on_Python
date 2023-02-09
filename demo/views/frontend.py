import aiohttp
import asyncpg
from aiohttp_jinja2 import template


@template('index.html')
async def index(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name}

async def post(request):
    conn = await asyncpg.connect('postgresql://postgres:vikaV1910@localhost:5432/demo')
    result = await conn.fetch("SELECT * FROM post")

    return aiohttp.web.Response(body=str(result))

