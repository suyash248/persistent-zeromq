import redis
import settings

print ("Initialization - Redis connection pool")
redis_conn_pool = redis.ConnectionPool(host=settings.REDIS_CONF.get('REDIS_HOST', 'localhost'),
                        port=settings.REDIS_CONF.get('REDIS_PORT', 6379), db=settings.REDIS_CONF.get('REDIS_DB', 0),
                        password=settings.REDIS_CONF.get('REDIS_PASSWORD', ''))
redis_connection = redis.Redis(connection_pool=redis_conn_pool)