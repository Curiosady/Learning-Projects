from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
import csv


def write_csv(data):
    with open('auto_ru_ads.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['model'],
                         data['year'],
                         data['engine'],
                         data['power'],
                         data['gas'],
                         data['transmission'],
                         data['body'],
                         data['drive'],
                         data['color'],
                         data['mileage'],
                         data['price']))


def get_html(url_gen):
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    while True:
        try:
            driver.get(url_gen)
            html = driver.page_source
            driver.close()
            driver.quit()
        except TimeoutException:
            print('No Response. Try again...')
            continue
        else:
            break

    return html


def get_total_pages(html):
    soup = bs(html, 'html.parser')
    try:
        ads_on_page = len(soup.find_all('div', 'ListingItem-module__container'))
        total_ads = int(soup.find('span', 'ButtonWithLoader__content').text.split()[1])
        total_pages = total_ads // ads_on_page
    except:
        total_pages = 0

    return total_pages


def get_page_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', 'ListingItem-module__description')
    for item in items:
        try:
            model = item.find('a', 'Link ListingItemTitle-module__link').text
        except:
            model = ''
        try:
            year = item.find('div', 'ListingItem-module__year').text
        except:
            year = ''
        try:
            price = item.find('div', 'ListingItemPrice-module__content').text
        except:
            price = ''
        try:
            mileage = item.find('div', 'ListingItem-module__kmAge').text
        except:
            mileage = ''
        try:
            tech_summary = item.find_all('div', 'ListingItemTechSummary-module__cell')
            if len(tech_summary) != 0:
                engine = tech_summary[0].text.split('/')[0].split()[0]
                power = tech_summary[0].text.split('/')[1].split()[0]
                gas = tech_summary[0].text.split('/')[2]

                transmission = tech_summary[1].text
                body = tech_summary[2].text
                drive = tech_summary[3].text
                color = tech_summary[4].text
        except:
            engine = ''
            transmission = ''
            body = ''
            drive = ''
            color = ''
        data = {'model': model,
                'year': year,
                'engine': engine,
                'power': power,
                'gas': gas,
                'transmission': transmission,
                'body': body,
                'drive': drive,
                'color': color,
                'mileage': mileage,
                'price': price}
        write_csv(data)


def get_manufacturers(html):
    soup = bs(html, 'html.parser')
    manufacturers = []
    for a in soup.find_all('a', 'IndexMarks__item'):
        manufacturers.append(a['href'])

    return manufacturers


def main():
    manufacturers = get_manufacturers(get_html('https://auto.ru/moskva/'))
    for i in range(0, len(manufacturers)):
        man_url = str(manufacturers[i])[:-4]
        for j in range(1990, 2019):
            url = man_url + str(j) + '-year/used/' + '?sort=cr_date-desc&output_type=list&page='
            full_url = url + '1'
            total_pages = get_total_pages(get_html(full_url)) + 1
            for k in range(1, (total_pages + 1)):
                url_gen = url + str(k)
                html = get_html(url_gen)
                get_page_data(html)
                print(str(k) + ' of ' + str(total_pages) + ' in ' + manufacturers[i][:-4] + ' for ' + str(j) + ' year')


if __name__ == '__main__':
    main()
