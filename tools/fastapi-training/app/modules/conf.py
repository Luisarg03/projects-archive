from fastapi import Query
from fastapi_pagination.cursor import CursorPage
from .database import SessionLocal


def cursor_confs():
    cursor_confs = CursorPage.with_custom_options(
        size=Query(5),
    )

    return cursor_confs


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
