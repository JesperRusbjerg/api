# script used to convert

import zeeguu.core
from zeeguu.core.model import User

session = zeeguu.core.db.session

for user in User.query.all():
    print (f'updating user {user}')
    user.password = user.password.hex().encode('utf-8')
    user.password_salt = user.password_salt.hex().encode('utf-8')
    session.add(user)
    session.commit()

# now make sure to change the column type of the
# table to string.
