from aiohttp import web
import json

async def handle_get(request):
    response_data = {
        'message': 'Hello, World!',
        'path': request.path
    }
    return web.Response(text=json.dumps(response_data), content_type='application/json')

async def handle_post(request):
    try:
        data = await request.json()
    except Exception:
        return web.Response(status=400, text='{"error": "Invalid JSON"}', content_type='application/json')

    response_data = {
        'message': 'Data received',
        'received_data': data
    }
    return web.Response(text=json.dumps(response_data), content_type='application/json')

app = web.Application()
app.router.add_get('/', handle_get)
app.router.add_post('/', handle_post)

if __name__ == '__main__':
    web.run_app(app, port=8080)