from exts import db
# from app import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)

    def __repr__(self):
        return '<User(name=%s)>' % self.name


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id'))

    publisher = db.relationship('User', backref='articles')

    def __repr__(self):
        return '<Article(title=%s)>' % self.title

# db.drop_all()
# db.create_all()
# user = User(name='kano')
# article1 = Article(title='inoji no name.')
# article2 = Article(title='ko no seigai..')
# user.articles.append(article1)
# user.articles.append(article2)
# db.session.add(user)
# db.session.commit()
# print(User.query.all())
# print(Article.query.filter(Article.id==2).all())