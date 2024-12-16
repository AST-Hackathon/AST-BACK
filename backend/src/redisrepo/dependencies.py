from src.app_config.config_redis import RedisRepository


async def get_redis_repo() -> RedisRepository:
    return await RedisRepository.connect()


# async def get_redis_repo(
#     redis_repo: RedisRepository = Depends(lambda: get_redis_repo.redis_repo),
# )-> RedisRepository:
#     return redis_repo

# s
