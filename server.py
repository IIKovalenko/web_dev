from flask import Flask, render_template
from weather import weather_by_city
from python_org_news import get_python_news

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Прогноз погоды'
    weather = weather_by_city('Moscow,Russia')
    print(weather)
    news_list = get_python_news()
    #if weather:
        #weather_text = f'Погода: {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}'
    #else:
        #weather_text = 'Сервер с погодой временно недоступен'
    return render_template("index.html", page_title=title, weather=weather, news_list=news_list)
if __name__ == '__main__':
    app.run(debug=True)


