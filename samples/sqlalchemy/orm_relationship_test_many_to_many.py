from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, desc, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime

DB_URI = 'mysql+pymysql://root:skywalker@127.0.0.1:3306/first_alchemy?charset=utf8'
db_engine = create_engine(DB_URI)
Base = declarative_base(bind=db_engine)
session = sessionmaker(db_engine)()


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<User(name:%s)>' % self.name


article_tag = Table('article_tag', Base.metadata,
                    Column('article_id', Integer, ForeignKey('articles.id')),
                    Column('tag_id', Integer, ForeignKey('tags.id'))
                    )


class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(Text, nullable=False)
    create_time = Column(DateTime, default=datetime.now)
    tags = relationship('Tag', backref='articles', secondary=article_tag)

    def __repr__(self):
        return '<Article(title:%s)>' % self.title


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()
    article1 = Article(title='first blog. python project!')
    article2 = Article(title='you favoriate blog')

    tag1 = Tag(name='python ')
    tag2 = Tag(name='happy ')

    article1.tags.append(tag1)
    article1.tags.append(tag2)

    article2.tags.append(tag1)
    article2.tags.append(tag2)
    session.add(article1)
    session.add(article2)
    session.commit()


def operation():
    article = session.query(Article).first()
    print(article.tags)
    tag = session.query(Tag).first()
    print(tag.articles)


if __name__ == '__main__':
    # db_init()
    operation()
