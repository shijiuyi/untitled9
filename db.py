from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


engine = create_engine('postgresql+psycopg2://postgres:123456789'
                       '@localhost/testdb')
# 创建dbsession类型,scoped_session类并没有继承Session,但是却又它的所有方法
dbsession = scoped_session(sessionmaker(bind=engine))
# 生成orm基类
Base = declarative_base(engine)

# 在对表数据进行增删改查之前，先需要建立会话，建立会话之后才能进行操作
Session = sessionmaker(engine)
# 打开会话
session = Session()

# 我们用类来表示数据库里面的表
# 这些表的类都继承于我们的Base基类。
# 在类里面我们定义一些属性，这个属性通过映射，就对应表里面的字段
class Login_info(Base):
    __tablename__ = 'login_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(20), nullable=False, unique=True)
    password = Column(String(50), nullable=False)

    # repr()方法显示一个可读字符串,实例返回的内容
    def __repr__(self):
        return '<Login_info: %s %s %s>' % (self.uname, self.password, self.id)


Base.metadata.create_all()

"""# add
person = User(uname='buodng', password='1q2w3e4r')
session.add(person)

# 加多条
session.add_all([
    User(uname='tuple', password='222'),
    User(uname='which', password='333')
])
session.commit()

rows = session.query(User).all()
rows = session.query(User).first()

if __name__ == '__main__':
    connection = engine.connect()
    # 验证是否连接成功
    results = connection.execute('select 1')
    print(results.fetchone())"""


