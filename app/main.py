import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


app = FastAPI()


class ProfileSchema(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str


@app.get('/profile', response_model=ProfileSchema, response_class=JSONResponse)
def get_profile(request: Request) -> JSONResponse:
    if 'X-UserId' not in request.headers:
        raise HTTPException(status_code=401, detail='Unauthorized')

    data = {
        'id': request.headers['X-UserId'],
        'username': request.headers['X-User'],
        'email': request.headers['X-Email'],
        'first_name': request.headers['X-First-Name'],
        'last_name': request.headers['X-Last-Name'],
    }
    content = ProfileSchema.parse_obj(data).dict()
    return JSONResponse(content, status_code=200)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
