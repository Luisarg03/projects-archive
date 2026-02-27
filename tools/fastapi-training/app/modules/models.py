from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Float, Integer

Base = declarative_base()


class UsersApi(Base):
    __tablename__ = "users_api"
    row_id = Column(Integer, primary_key=True)
    username = Column(String)
    full_name = Column(String)
    email = Column(String)
    password = Column(String)
    disabled = Column(String)


class DataScienceSalary(Base):
    __tablename__ = "data_sciences_salaries"
    row_id = Column(Integer, primary_key=True)
    work_year = Column(Integer)
    experience_level = Column(String)
    employment_type = Column(String)
    job_title = Column(String)
    salary = Column(Integer)
    salary_currency = Column(String)
    salary_in_usd = Column(Integer)
    employee_residence = Column(String)
    remote_ratio = Column(Integer)
    company_location = Column(String)
    company_size = Column(String)


class PokemonDataMaster(Base):
    __tablename__ = 'pokemon_tcg_data_master'
    row_id = Column(Integer, primary_key=True)
    id = Column(String)
    set = Column(String)
    series = Column(String)
    publisher = Column(String)
    generation = Column(String)
    release_date = Column(String)
    artist = Column(String)
    name = Column(String)
    set_num = Column(String)
    types = Column(String)
    supertype = Column(String)
    subtypes = Column(String)
    level = Column(String)
    hp = Column(Float)
    evolvesFrom = Column(String)
    evolvesTo = Column(String)
    abilities = Column(String)
    attacks = Column(String)
    weaknesses = Column(String)
    retreatCost = Column(String)
    convertedRetreatCost = Column(Float)
    rarity = Column(String)
    flavorText = Column(String)
    nationalPokedexNumbers = Column(String)
    legalities = Column(String)
    resistances = Column(String)
    rules = Column(String)
    regulationMark = Column(String)
    ancientTrait = Column(String)
