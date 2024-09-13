from redis.asyncio import Redis

import conf


session_storage = Redis.from_url(
    url=f"redis://{conf.REDIS_HOSTNAME}:6379/0"
)
