from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import get_session
from .models import Profile
from .models import Session as AuthSession
from .schemas import LoginSchema, ProfileSchema


router = APIRouter()


@router.post('/register', response_model=ProfileSchema, response_class=JSONResponse)
async def register(
    schema: ProfileSchema, session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    content: dict = schema.dict()
    content.pop('id')

    try:
        result_id = await crud.create(session, Profile, content)
    except IntegrityError:
        raise HTTPException(status_code=400, detail='The data must be unique')

    content.update({'id': result_id})
    return JSONResponse(content, status_code=status.HTTP_201_CREATED)


@router.put('/edit-profile', response_model=ProfileSchema, response_class=JSONResponse)
async def edit_profile(
    schema: ProfileSchema,
    session: AsyncSession = Depends(get_session),
    session_id: str = Cookie(...),
) -> JSONResponse:
    content: dict = schema.dict()
    content.pop('id')

    auth_session = await crud.read(
        session, AuthSession, [and_(AuthSession.id == session_id)]
    )

    if not auth_session:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not signed in')

    profile_id = auth_session.payload['id']

    try:
        await crud.update(session, Profile, profile_id, content)
    except IntegrityError:
        raise HTTPException(status_code=400, detail='The data must be unique')

    payload = {**content, **{'id': profile_id}}
    await crud.update(session, AuthSession, session_id, {'payload': payload})

    content.update({'id': profile_id})
    return JSONResponse(content, status_code=status.HTTP_200_OK)


@router.post('/login', response_class=JSONResponse)
async def login(
    schema: LoginSchema, session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    profile = await crud.read(
        session, Profile, [and_(Profile.username == schema.username)]
    )

    if not profile:
        raise HTTPException(status_code=401, detail='The username does not exist')

    if profile.password != schema.password:
        raise HTTPException(status_code=401, detail='The wrong password')

    payload = {
        'id': profile.id,
        'username': profile.username,
        'email': profile.email,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
    }

    try:
        auth_session_id = await crud.create(session, AuthSession, {'payload': payload})
    except IntegrityError:
        raise HTTPException(status_code=400, detail='The data must be unique')

    response = JSONResponse(status_code=status.HTTP_200_OK)
    response.set_cookie('session_id', str(auth_session_id), httponly=True)
    return response


@router.get('/logout', response_class=JSONResponse)
async def logout(
    session_id: str = Cookie(...), session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    auth_session = await crud.read(
        session, AuthSession, [and_(AuthSession.id == session_id)]
    )

    if not auth_session:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not signed in')

    await crud.delete(session, AuthSession, [and_(AuthSession.id == session_id)])

    response = JSONResponse(status_code=status.HTTP_200_OK)
    response.set_cookie('session_id', '', expires=0)
    return response


@router.get('/auth', response_class=JSONResponse)
async def auth(
    session_id: str = Cookie(...), session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    auth_session = await crud.read(
        session, AuthSession, [and_(AuthSession.id == session_id)]
    )

    if not auth_session:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Not signed in')

    headers = {
        'X-UserId': auth_session.payload['id'],
        'X-User': auth_session.payload['username'],
        'X-Email': auth_session.payload['email'],
        'X-First-Name': auth_session.payload['first_name'],
        'X-Last-Name': auth_session.payload['last_name'],
    }
    return JSONResponse(status_code=status.HTTP_200_OK, headers=headers)
