from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from error import InvalidUsage, EmptyParamError

async def homepage(request):
    
    return JSONResponse({'hello': 'world'})

async def raise_except(request):
    
    param = None
    method = 'get'
    try:
        
        if param == None:
            raise EmptyParamError(status_code=403, message="value of b is zero")
        if method == 'get':
            raise InvalidUsage(status_code=400, message="Invalid usage")
            
    except InvalidUsage as e:
        return JSONResponse({'error_message': str(e.message), 'status_code': e.status_code})
    except EmptyParamError as e:
        return JSONResponse({'error_message': str(e.message), 'status_code': e.status_code})
        
    
    


routes = [
    Route("/", endpoint=homepage, methods=['GET'])
    Route("/exception", endpoint=raise_except, methods=['GET'])
]

app = Starlette(routes=routes,debug=True)
