# Прогнозирование стоимости подержанного автомобиля в Москве

### Постановка задачи

Идеей проекта является построение модели, которую можно использовать для оценки стоимости подержанного автомобиля. 

Для маркетплейсов по продаже автомобилей такая модель могла бы лечь в основу рекомендательной системы при размещении объявлений, а рядовые автомобилисты могли бы использовать эту модель для оценки остаточной стоимости автомобиля и выбора наиболее благоприятного момента для продажи.

### Структура проекта

- data
	* [auto_ru_df.csv](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/data/auto_ru_df.csv)  - сырой датасет после парсинга
	* [preprocessed_auto_ru_df.csv](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/data/preprocessed_auto_ru_df.csv) - датасет после предобработки
- notebooks
	* [ Preprocessing.ipynb](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/notebooks/Preprocessing.ipynb) - тетрадка с предобработкой датасета
	* [EDA.ipynb](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/notebooks/EDA.ipynb) - визуальный анализ данных
	* [Predictions.ipynb](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/notebooks/Predictions.ipynb) - построение моделей и их оценка
- scripts
	* [web_scraper.py](https://github.com/Curiosady/Learning-Projects/blob/master/Auto.ru%20Car%20Price%20Prediction/scripts/web_scraper.py) - скрипт для скрапа данных с auto.ru

### Описание набора данных

Датасет был получен с помощью скрипта web_scraper.py. Получение html-страницы сделано с помощью библиотеки Selenium, парсинг осуществлен через библиотеку BeautifulSoup. Парсились объявления с сайта auto.ru в категории подержанные автомобили, территориально расположенные в Москве и 200-километровой окружности.

Набор данных после препроцессинга содержит в себе 113154 запись и 11 признаков: 4 числовых, 6 категориальных и целевой.

* car_description - марка, модель и поколение автомобиля
* year - год выпуска
* engine - объем двигателя в литрах
* power - мощность двигателя в лошадиных силах
* gas - типа используемого топлива
* transmission - тип коробки передач
* body -  форма кузова
* drive - привод
* color - цвет кузова
* mileage - пробег
* price - цена
