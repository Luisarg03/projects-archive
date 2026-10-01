from fastapi import APIRouter, Depends
from modules import crud, schemas
from modules.conf import cursor_confs, get_db
from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate
from modules.security import get_current_user

CursorPage = cursor_confs()
router = APIRouter()


@router.get("/getdata/pokemon/", response_model=CursorPage[schemas.PokemonDataMaster])
def read_pokemon(db: Session = Depends(get_db), current_user: str = Depends(get_current_user)) -> CursorPage[schemas.PokemonDataMaster]:
    query = crud.get_data_pokemon(db)
    return paginate(query)
