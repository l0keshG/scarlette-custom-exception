from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

from error import InvalidUsage, EmptyParamError

async def homepage(request):

    a=1
    b=0

    try:
        if a==1:
            raise InvalidUsage(400, "Invalid usage")

        if b == 0:
            raise EmptyParamError(403, "value of b is zero")
    except InvalidUsage as e:
        return JSONResponse({'error_message': str(e.message), 'status_code': e.status_code})
    except EmptyParamError as e:
        return JSONResponse({'error_message': str(e.message)})
        
        
    return JSONResponse({'hello': 'world'})


routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(routes=routes,debug=True)