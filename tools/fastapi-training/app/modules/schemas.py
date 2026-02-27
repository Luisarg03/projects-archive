from pydantic import BaseModel
from typing import Optional


# Esquema para la lectura de datos (por ejemplo, para respuestas de la API)
class UsersApi(BaseModel):
    username: str
    password: str
    disabled: bool

    class Config:
        orm_mode = True


class DataScienceSalary(BaseModel):
    row_id: int
    work_year: Optional[int]
    experience_level: Optional[str]
    employment_type: Optional[str]
    job_title: Optional[str]
    salary: Optional[int]
    salary_currency: Optional[str]
    salary_in_usd: Optional[int]
    employee_residence: Optional[str]
    remote_ratio: Optional[int]
    company_location: Optional[str]
    company_size: Optional[str]

    class Config:
        orm_mode = True


class PokemonDataMaster(BaseModel):
    row_id: int
    id: Optional[str]
    set: Optional[str]
    series: Optional[str]
    publisher: Optional[str]
    generation: Optional[str]
    release_date: Optional[str]
    artist: Optional[str]
    name: Optional[str]
    set_num: Optional[str]
    types: Optional[str]
    supertype: Optional[str]
    subtypes: Optional[str]
    level: Optional[str]
    hp: Optional[float]
    evolvesFrom: Optional[str]
    evolvesTo: Optional[str]
    abilities: Optional[str]
    attacks: Optional[str]
    weaknesses: Optional[str]
    retreatCost: Optional[str]
    convertedRetreatCost: Optional[float]
    rarity: Optional[str]
    flavorText: Optional[str]
    nationalPokedexNumbers: Optional[str]
    legalities: Optional[str]
    resistances: Optional[str]
    rules: Optional[str]
    regulationMark: Optional[str]
    ancientTrait: Optional[str]

    class Config:
        orm_mode = True
