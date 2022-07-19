# THIRD PARTY IMPORTS
from contextlib import asynccontextmanager
import cx_Oracle_async

# PROJECT IMPORTS
from func.src.infrastructure.env_config import config


class OracleInfrastructure:

    pool = None

    @classmethod
    async def _get_pool(cls):
        if cls.pool is None:
            cls.pool = await cx_Oracle_async.create_pool(
                user=config("ORACLE_BASE_USER"),
                password=config("ORACLE_BASE_PASSWORD"),
                min=2,
                max=100,
                increment=1,
                dsn=cx_Oracle_async.makedsn(
                    config("ORACLE_BASE_DSN"),
                    config("ORACLE_BASE_PORT"),
                    service_name=config("ORACLE_BASE_SERVICE_US"),
                ),
                encoding=config("ORACLE_ENCODING"),
            )
        return cls.pool

    @classmethod
    @asynccontextmanager
    async def get_connection(cls):
        pool = await cls._get_pool()
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                yield cursor
                await conn.commit()
