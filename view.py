import traceback
import tornado
from tornado import web
from db import engine, Login_info, dbsession, session
import log
import hashlib


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.db = dbsession()


# 逻辑处理模块
class LoginHander(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('templates/login.html')

    def post(self, *args, **kwargs):
        # 验证登录
        # 获取用户登录的用户名，密码
        username = self.get_argument('username')
        password = self.get_argument('password')

        password_md5 = hashlib.md5(password.encode()).hexdigest()
        query = self.db.query(Login_info).filter(
            Login_info.uname == username, Login_info.password == password_md5).all()

        try:
            if query:
                self.render('templates/index.html')
            else:
                self.render('templates/error.html', info={
                    'info': '用户名/密码不正确'
                })
        except:
            traceback.print_exc()


class RegisterHandler(BaseHandler):
    def post(self, *args, **kwargs):
        # id = self.get_argument('id')
        username = self.get_argument('username')
        password = self.get_argument('password')
        password1 = self.get_argument('password1')

        try:
            if username and password:
                if username.__len__() < 9 and username.__len__() >= 0 and \
                        password.__len__() < 9 and password.__len__() >= 0:
                    password_md5 = hashlib.md5(password.encode()).hexdigest()
                    query = self.db.query(Login_info.uname).filter(
                        Login_info.uname == username).all()
                    print(query)

                    if ('username',) == query:
                        self.render('templates/error.html', info={
                            'info': '用户名已存在'
                        })
                    else:
                        if password == password1:
                            # 两种添加方法
                            # info = Login_info(uname=username, password=password)
                            # session.add(info)
                            session.add(Login_info(uname=username, password=password_md5))
                            session.commit()
                            session.close()
                            self.render('templates/login.html')
                        else:
                            self.render('templates/error.html', info={
                                'info': '密码不一致'
                            })
                else:
                    self.render('templates/error.html', info={
                        'info': '用户名和密码长度在0~9之间'
                    })
            else:
                self.render('templates/error.html', info={
                    'info': '请输入用户名和密码'
                })
        except:
            traceback.print_exc()
            session.rollback()

    def get(self, *args, **kwargs):
        self.render('templates/register.html')


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html')

logger = log.logger
logger.warning('msg')
