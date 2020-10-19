from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

DB_URI = 'mysql+pymysql://root:skywalker@127.0.0.1:3306/first_alchemy?charset=utf8'
db_engine = create_engine(DB_URI)
Base = declarative_base(bind=db_engine)
session = sessionmaker(db_engine)()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<User(name:%s)>' % self.name

# User <----> UserExtend 一对一 uselist
class UserExtend(Base):
    __tablename__ = 'userextends'
    id = Column(Integer, primary_key=True, autoincrement=True)
    info = Column(Text, nullable=False)
    uid = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', backref=backref('userextend', uselist=False))
    def __repr__(self):
        return '<UserExtend(info: %s)>' % self.info
        
# User <----> Article 一对多
class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    author = Column(Integer, ForeignKey('users.id'))

    # cascade默认为 'save-update, merge'，删除article,对应的user行无影响。删除user,对应article.author设置为null
    # publisher = relationship('User', backref='articles')
    # 删除article,对应的user行也整个删除。删除user,对应article.author设置为null
    # publisher = relationship('User', backref='articles', cascade='save-update, delete')
    # 删除article,对应的user行也整个删除。删除user,对应article行整个删除
    # publisher = relationship('User', backref=backref('articles', cascade='save-update, delete'),
    #                         cascade='save-update, delete')
    # 删除article,对应的user行无影响。删除user,对应article行整个删除
    # 将user关联值为空，与之关联的article整个被删除
    # publisher = relationship('User', backref=backref('articles', cascade='save-update, delete, delete-orphan'),
    #                         cascade='save-update')
    # merge合并，以id为标记，关联的表的数据也会合并。不设置merge则不会合并关联的数据
    # publisher = relationship('User', backref=backref('articles', cascade='save-update, delete, delete-orphan, merge'),
    #                         cascade='save-update')
    # expunge移除操作时，关联的对象也会被移除。在session中移除，不是数据库中删除
    # publisher = relationship('User', backref=backref('articles', cascade='save-update'),cascade='save-update')
    # all = 'save-update, merge, refresh-expire, expunge, delete''
    publisher = relationship('User', backref=backref('articles', cascade='all'), cascade='save-update')

    # refresh-expire Session.expire()操作时，从parent延伸到关联对象，事务中功能
    def __repr__(self):
        return '<Article(title:%s)>' % self.title


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

    article1 = Article(title='python flask study 1')
    user1 = User(name='kano')
    # article1.author = user1 #!!!!!!error
    article1.publisher = user1
    session.add(user1)
    # user1.articles.append(article1)
    # session.add(user1)
    # session.add_all([article1, user1])
    session.commit()


def operation():
    user1 = session.query(User).filter(User.id == 1).first()
    print(user1)
    print(user1.articles)
    session.delete(user1)
    session.commit()
    # test orphan
    # user1.articles = []  # 设置关联为空
    # article1 = session.query(Article).filter(Article.id==1).first()
    #session.delete(article1)  #
    #test merge
    # user2 = User(id=1, name='natsume')
    # article2 = Article(id=1, title='go go go test!')
    # user2.articles.append(article2)
    # session.merge(user2)
    # session.commit()
    # test expunge
    # user3 = User(name='natsume')
    # article3 = Article(title='go go go expunge!')
    # user3.articles.append(article3)
    # session.add(user3)
    # session.add(article3)
    # session.expunge(user3)
    # session.commit()

    # print(article1)
    # print(article1.publisher)


if __name__ == '__main__':
    # db_init()
    operation()
