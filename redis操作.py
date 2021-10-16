from redis import StrictRedis
redis = StrictRedis(host = 'localhost', port = 6379, db = 2)
urls = [f'http://www.cnoil.com/gjs/list_{i}.html' for i in range(1,3)]
for url in urls:
    redis.rpush("cnoil:url",url)