import asyncio
from typing import Optional
from hashlib import sha1

from func.src.repositories.base_repository.oracle.base import OracleBaseRepository
from func.src.repositories.cache.repository import RepositoryRedis


class SinacorTypesRepository(OracleBaseRepository):
    cache = RepositoryRedis

    @classmethod
    async def get_county_name_by_id(cls, id: int) -> Optional[str]:
        sql = f"""
            SELECT NOME_MUNI
            FROM CORRWIN.TSCDXMUNICIPIO
            WHERE NUM_SEQ_MUNI = {id}
        """
        tuple_result = await cls.query_with_cache(sql=sql)
        if tuple_result:
            return tuple_result[0][0]

    @classmethod
    async def query_with_cache(cls, sql: str) -> list:
        _sha1 = sha1()
        _sha1.update(str(sql).encode())
        partial_key = _sha1.hexdigest()
        key = f"sinacor_types:{partial_key}"
        value = await cls.cache.get(key=key)
        if not value:
            partial_value = await cls.query(sql=sql)
            value = {"value": partial_value}
            await cls.cache.set(key=key, value=value, ttl=86400)

        value = value.get("value")
        return value
