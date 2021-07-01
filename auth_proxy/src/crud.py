from typing import Union

from sqlalchemy import insert, select
from sqlalchemy import delete as delete_stmt
from sqlalchemy import update as update_stmt
from sqlalchemy.ext.asyncio import AsyncSession

from .db import Base


async def create(
    session: AsyncSession,
    entity: Base,
    data: dict,
) -> int:
    stmt_create = insert(entity).values(**data).returning(entity.id)
    result = await session.execute(stmt_create)
    await session.commit()
    return result.scalars().first()


async def read(
    session: AsyncSession,
    entity: Base,
    filter_: list,
) -> Base:
    stmt = select(entity).filter(*filter_)
    result = await session.execute(stmt)
    return result.scalars().first()


async def update(
    session: AsyncSession,
    entity: Base,
    entry_id: Union[int, str],
    data: dict,
) -> None:
    stmt = update_stmt(entity).where(entity.id == entry_id).values(**data)
    await session.execute(stmt)
    await session.commit()


async def delete(
    session: AsyncSession,
    entity: Base,
    filter_: list,
) -> None:
    stmt = delete_stmt(entity).where(*filter_)
    await session.execute(stmt)
    await session.commit()
