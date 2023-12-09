import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

class CarScraper:
    def __init__(self):
        self.final_result = []

    def scrape(self):
        locations = ['Bangalore', 'Chennai', 'Delhi', 'Faridabad', 'Ghaziabad', 'Gurgaon', 'Hyderabad', 'Mumbai',
                                 'Noida', 'Pune']
        for location in locations:

            if location == 'Bangalore':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Bangalore%5C%22%2C%5C%22selectedCityId%5C%22:1}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; _gat_UA-133540600-1=1; _ga=GA1.1.118202895.1696779968; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; analytics_session_id.last_access=1696780164713; _clsk=140bvan|1696780164776|6|1|u.clarity.ms/collect; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780165.44.0.0',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
            elif location == 'Chennai':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780174.35.0.0; _clsk=140bvan|1696780799610|9|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Chennai%5C%22%2C%5C%22selectedCityId%5C%22:10}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696780803794',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Delhi':
                header = {
                    'Cookie':'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _gat_UA-133540600-1=1; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780808.59.0.0; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _clsk=140bvan|1696780809116|10|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Delhi%5C%22%2C%5C%22selectedCityId%5C%22:3}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696780849249',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Faridabad':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780851.16.0.0; _clsk=140bvan|1696780853354|11|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Faridabad%5C%22%2C%5C%22selectedCityId%5C%22:8}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696780898552',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Ghaziabad':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _gat_UA-133540600-1=1; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780901.59.0.0; _clsk=140bvan|1696780902484|12|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Ghaziabad%5C%22%2C%5C%22selectedCityId%5C%22:7}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696780931244',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Gurgaon':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780934.26.0.0; _clsk=140bvan|1696780935052|13|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Gurgaon%5C%22%2C%5C%22selectedCityId%5C%22:5}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696780966686',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Hyderabad':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _gat_UA-133540600-1=1; _ga=GA1.1.118202895.1696779968; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696780970.59.0.0; _clsk=140bvan|1696780970931|14|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Hyderabad%5C%22%2C%5C%22selectedCityId%5C%22:9}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696781003868',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Mumbai':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696781007.22.0.0; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _clsk=140bvan|1696781008409|15|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Mumbai%5C%22%2C%5C%22selectedCityId%5C%22:2}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696781040677',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Noida':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _gat_UA-133540600-1=1; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696781043.59.0.0; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _clsk=140bvan|1696781044487|16|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Noida%5C%22%2C%5C%22selectedCityId%5C%22:4}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696781070742',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            elif location == 'Pune':
                header = {
                    'Cookie': 'source=web; eventTrackerUserId=f6ec3d29-a86a-4293-a77a-e44af683bef2; reduxPersistIndex=[%22persist:new-ackodrive-front%22]; ajs_anonymous_id=f6ec3d29-a86a-4293-a77a-e44af683bef2; _gcl_au=1.1.635965145.1696779968; _gid=GA1.2.1322553059.1696779968; _fbp=fb.1.1696779968298.960702582; _clck=rerghj|2|ffo|0|1376; analytics_session_id=1696779974895; _gat_UA-133540600-1=1; _ga=GA1.1.118202895.1696779968; _ga_0X18GKRF28=GS1.1.1696779968.1.1.1696781072.30.0.0; _uetsid=cc4bdb5065f111eeb7d09371d7cb839c; _uetvid=cc4c1d0065f111eea92ff1bf28f43ad5; _clsk=140bvan|1696781074371|17|1|u.clarity.ms/collect; persist%3Anew-ackodrive-front={%22cities%22:%22{%5C%22selectedCity%5C%22:%5C%22Pune%5C%22%2C%5C%22selectedCityId%5C%22:6}%22%2C%22membership%22:%22{%5C%22membershipPhone%5C%22:%5C%22%5C%22}%22%2C%22myAccount%22:%22{%5C%22myDeals%5C%22:false%2C%5C%22cashBackQuoteId%5C%22:%5C%22%5C%22}%22%2C%22packageService%22:%22{}%22%2C%22_persist%22:%22{%5C%22version%5C%22:-1%2C%5C%22rehydrated%5C%22:true}%22}; analytics_session_id.last_access=1696781098087',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

            for page in range(1,6):
                url = f'https://ackodrive.com/cars/page/{page}/'

                response = requests.get(url,headers = header)
                # print(response)

                page_source = response.content

                jsoup =BeautifulSoup(page_source,'html.parser')

                head = jsoup.find('div', attrs={'class':'styles__CarListWrapper-sc-dccd5557-2 fMgIaI'})
                if head is None:
                    continue
                result = head.find_all('div', attrs={'class':'styles__Wrapper-sc-cbcba852-0 jtAUjc'})



                for div in result:
                    dummy = dict()
                    a = div.find('a', attrs={'class': 'styles__AnchorTagWithoutUnderline-sc-ff1d2337-32 enHGMk'})
                    h3 = div.find('h3', attrs={'class': 'styles__ModelTitle-sc-ff1d2337-4 fxObep'})
                    body = div.find_all('p', attrs={'class': 'styles__ParaWithoutMargins-sc-ff1d2337-33 cvFhPe'})
                    # print(body)
                    h4 = div.find('h4', attrs={'class': 'styles__VariantTitle-sc-ff1d2337-10 jrtfkd'})
                    for_city = div.find('div', attrs={'class': 'styles__CityName-sc-ff1d2337-17 hJZuQt'})
                    for_price = div.find('div', attrs={'class': 'styles__Price-sc-ff1d2337-18 CHHgf'})

                    name = h3.text
                    link = a['href']
                    body_type = body[0].get_text()
                    model = body[1].get_text()
                    variant = body[2].get_text()
                    variant_title = h4.text
                    fuel = body[3].text
                    gear = body[4].text
                    colors = body[5].text
                    city = for_city.text
                    price = for_price.text

                    dummy['Name'] = name
                    dummy['Link'] = link
                    dummy['Body Type'] = body_type
                    dummy['Model'] = model
                    dummy['Model Variant'] = variant
                    dummy['Variant Title'] = variant_title
                    dummy['Fuel Type'] = fuel
                    dummy['Gear Type'] = gear
                    dummy['Available Colors'] = colors
                    dummy['City'] = city
                    dummy['Price'] = price

                    self.final_result.append(dummy)

# print(final_result)

if __name__ == '__main__':
    car_scraper_obj = CarScraper()
    car_scraper_obj.scrape()

    final_result = car_scraper_obj.final_result
    df = pd.DataFrame(final_result)
    today = datetime.today().strftime('%d-%m-%y ---%H-%M')
    df.to_csv("D:\\$PYTHON\\cars\\" + today + " Ackodrive cars.csv", index=False)

