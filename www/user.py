import orm, asyncio
from models import User, Blog, Comment


@asyncio.coroutine
def init(loop):
    yield from orm.create_pool(loop=loop, user='www-data', password='www-data',db='awesome')
#    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
#    b = Blog(user_id='1', user_name='名字2', content='这是我的第一个博客', user_image='', name='Test Blog', summary='summary')
#   b1 = Blog(user_id='2', user_name='名字2', content='这是我的第一个博客', user_image='', name='Something New', summary='summary')
#    b2 = Blog(user_id='3', user_name='名字2', content='这是我的第一个博客', user_image='', name='Learn Swift', summary='summary')
    c = Comment(id='1', blog_id='1', user_id='4', user_name="usercomment", user_image='', content="first comment...")
#    yield from u.save()
    yield from c.save()
#    yield from b1.save()
 #   yield from b2.save()




loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
