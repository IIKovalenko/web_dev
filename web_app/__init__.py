from flask import Flask, render_template
from web_app.weather import weather_by_city
from web_app.python_org_news import get_python_news


def create_app():


    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Прогноз погоды'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        print(weather)
        news_list = get_python_news()
        #if weather:
            #weather_text = f'Погода: {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}'
        #else:
            #weather_text = 'Сервер с погодой временно недоступен'
        return render_template("index.html", page_title=title, weather=weather, news_list=news_list)


    return app


