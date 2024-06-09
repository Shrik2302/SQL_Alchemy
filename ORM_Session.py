from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ORM import Cookie
engine = create_engine("postgresql+psycopg2://postgres:root@localhost/basic", echo=True)

Session = sessionmaker(bind=engine)

session = Session()

"""
### Single insert ###
cc_cookie = Cookie(cookie_name = 'chocolate chip',
                   cookie_recipe_url = 'http://some.aweso.me/cookie/recipe.html',
                   cookie_sku = 'CC02',
                   quantity = 112,
                   unit_cost = 10
                   )
session.add(cc_cookie)
session.commit()
"""

"""
### Multiple insert
dcc = Cookie(cookie_name = 'dark chocolate chip',
             cookie_recipe_url = 'http://some.aweso.me/cookie/recipe_dark.html',
             cookie_sku = 'CC02',
             quantity = 5,
             unit_cost = 2)

mcc = Cookie(cookie_name='molasses',
             cookie_recipe_url = 'http://some.aweso.me/cookie/recipe_molasses.html',
             cookie_sku = 'MOL01',
             quantity = 5,
             unit_cost = 3)

session.add(dcc)
session.add(mcc)
session.flush() # it dosen't perform database commit
print(dcc.cookie_id)
print(mcc.cookie_id)
"""

"""
### Bulk inserting multiple column ###
c1 = Cookie(cookie_name='peanut butter',
            cookie_recipe_url='http://some.aweso.me/cookie/peanut.html',
            cookie_sku='PB01',
            quantity=24,
            unit_cost=0.25)
c2 = Cookie(cookie_name='oatmeal raisin',
            cookie_recipe_url='http://some.okay.me/cookie/raisin.html',
            cookie_sku='EWW01',
            quantity=100,
            unit_cost=1.00)
session.bulk_save_objects([c1,c2])
session.commit()
print(c1.cookie_id)
"""


### Querying Data ###
# cookies = session.query(Cookie).all()
# print(cookies)

for cookie in session.query(Cookie):
    print(cookie.cookie_name)
