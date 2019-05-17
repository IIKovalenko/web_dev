from flask import Flask, render_template
from web_app.weather import weather_by_city
from web_app.model import db, News
from web_app.user.models import User

from flask_login import LoginManager, current_user, login_required
from web_app.user.views import blueprint as user_blueprint



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        title = 'Прогноз погоды'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        print(weather)
        news_list = News.query.order_by(News.published.desc()).all()
        #if weather:
            #weather_text = f'Погода: {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}'
        #else:
            #weather_text = 'Сервер с погодой временно недоступен'
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ'


    return app


