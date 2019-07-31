import busorm, asyncio
from busmodels import User, Order, Car


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop, user='bus', password='buspassword',db='busdatabase')
    u = User(name='Test', telephone='1234567', passwd='1234567890', image='about:blank')
#    b2 = Blog(user_id='3', user_name='名字2', content='这是我的第一个博客', user_image='', name='Learn Swift', summary='summary')

    yield from u.save()
 




loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
