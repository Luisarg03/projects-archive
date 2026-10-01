from sqlalchemy import BigInteger, Boolean, Column, Double, Integer, MetaData, String, Table, Text
from sqlalchemy.orm.base import Mapped

metadata = MetaData()


t_data_sciences_salaries = Table(
    'data_sciences_salaries', metadata,
    Column('work_year', Integer),
    Column('experience_level', String),
    Column('employment_type', String),
    Column('job_title', String),
    Column('salary', Integer),
    Column('salary_currency', String),
    Column('salary_in_usd', Integer),
    Column('employee_residence', String),
    Column('remote_ratio', Integer),
    Column('company_location', String),
    Column('company_size', String),
    Column('row_id', Integer)
)


t_pokemon_tcg_data_master = Table(
    'pokemon_tcg_data_master', metadata,
    Column('id', String),
    Column('set', String),
    Column('series', String),
    Column('publisher', String),
    Column('generation', String),
    Column('release_date', String),
    Column('artist', String),
    Column('name', String),
    Column('set_num', String),
    Column('types', String),
    Column('supertype', String),
    Column('subtypes', String),
    Column('level', String),
    Column('hp', Double(53)),
    Column('evolvesFrom', String),
    Column('evolvesTo', String),
    Column('abilities', String),
    Column('attacks', String),
    Column('weaknesses', String),
    Column('retreatCost', String),
    Column('convertedRetreatCost', Double(53)),
    Column('rarity', String),
    Column('flavorText', String),
    Column('nationalPokedexNumbers', String),
    Column('legalities', String),
    Column('resistances', String),
    Column('rules', String),
    Column('regulationMark', String),
    Column('ancientTrait', String),
    Column('row_id', Integer)
)


t_train_essays_v1 = Table(
    'train_essays_v1', metadata,
    Column('text', String),
    Column('label', Integer),
    Column('prompt_name', String),
    Column('source', String),
    Column('RDizzl3_seven', Boolean),
    Column('row_id', Integer)
)


t_users_api = Table(
    'users_api', metadata,
    Column('username', Text),
    Column('full_name', Text),
    Column('email', Text),
    Column('password', Text),
    Column('disabled', Text),
    Column('row_id', BigInteger)
)
