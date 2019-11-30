from models import User
from myapp import db

admin = User('admin', 'admin@sgcc.com.cn')
guest = User('guest', 'guest@163.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
