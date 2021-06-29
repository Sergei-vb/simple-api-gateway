from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .dependencies import get_session
from .schemas import LoginSchema, ProfileSchema


router = APIRouter()


@router.post("/register", response_model=ProfileSchema, response_class=JSONResponse)
async def register(
    schema: ProfileSchema, session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    pass
    return


@router.put("/edit-profile", response_model=ProfileSchema, response_class=JSONResponse)
async def edit_profile(
    schema: ProfileSchema, session: AsyncSession = Depends(get_session)
) -> JSONResponse:
    pass
    return


@router.post("/login")
async def login(schema: LoginSchema, session: AsyncSession = Depends(get_session)):
    pass
    return


@router.route("/logout", methods=['GET', 'POST'])
async def logout(request: Request, session: AsyncSession = Depends(get_session)):
    pass
    return


@router.get("/auth")
async def auth(request: Request, session: AsyncSession = Depends(get_session)):
    pass
    return
