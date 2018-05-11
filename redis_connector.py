import redis

config = dict(REDIS_HOST = "127.0.0.1", REDIS_PORT = 6379, REDIS_DB = 0)

print ("Initialization - Redis connection pool")
redis_conn_pool = redis.ConnectionPool(host=config.get('REDIS_HOST', 'localhost'),
                                   port=config.get('REDIS_PORT', 6379), db=config.get('REDIS_DB', 0),
                                   password=config.get('REDIS_PASSWORD', ''))
redis_connection = redis.Redis(connection_pool=redis_conn_pool)