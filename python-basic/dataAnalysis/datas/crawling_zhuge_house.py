import random
import requests
from lxml import etree
from config_map import city_area_dicts

def get_content_today(city='成都', area=''):
    starts = ['据某站数据显示','有数据显示','据了解']
    start = starts[random.randint(0, len(starts)-1)]

    if area is None or area == '':
        url = 'https://cd.fangjia.zhuge.com/'
    else:
        url = city_area_dicts[area]

    r = requests.get(url)

    datas = r.text

    html = etree.HTML(datas)

    #数据时间
    update_time = html.xpath('/html/body/div[5]/div[7]/div[2]/div[2]/div[3]/text()')[0]
    if update_time is None or update_time == '':
        update_time = '截止到目前'
    else:
        update_time = update_time.split('，')[-1]
        update_time = update_time.replace('更新时间', '截止至')

    #新上房源数
    today_new_hosuse_num = html.xpath('(.//div[@class="room-today-new"])/text()')
    print(today_new_hosuse_num)
    #新上房源与昨日相比
    room_price_up_or_down = html.xpath('(.//div[@class="room-price-up"]/span)[2]/text()')
    room_price_percent = html.xpath('(.//div[@class="room-price-up"]/span)[3]/text()')
    if len(room_price_up_or_down) == 0:
        room_price_up_or_down = html.xpath('(.//div[@class="room-price-low"]/span)[2]/text()')
        room_price_percent = html.xpath('(.//div[@class="room-price-low"]/span)[3]/text()')

    #今日降价房源
    today_hosuse_low = html.xpath('.//div[@class="room-today-low"]/text()')

    #均价
    average_price = html.xpath('(.//div[@class="average-price"]/p)[1]/text()')
    #环比
    price_up_or_low = html.xpath('(.//div[@class="average-price-up"]/span)[1]/text()')
    if len(price_up_or_low) > 0:
        relative = html.xpath('(.//div[@class="average-price-up"]/span)[2]/text()')
    else:
        price_up_or_low = html.xpath('(.//div[@class="average-price-low"]/span)[1]/text()')
        relative = html.xpath('(.//div[@class="average-price-low"]/span)[2]/text()')

    #7天信息成交套数
    # /html/body/div[5]/div[7]/div[2]/div[2]/div[1]/div[2]/div[1]
    seven_day_nums = html.xpath('(.//div[@class="transfer-area"])/text()')
    transfer_lastday = html.xpath('((.//div[@class="transfer-lastweek"])[4])/span[2]/text()')
    print(seven_day_nums, transfer_lastday)

    content = '''
    {}，{}，成都{}二手房均价为{}元/平方米，环比上月{}，
    {}，与昨日相比{}，{}。
    成都二手房{}，相比昨日{}。
    然而实际成交价等更具有实际意义的数据大多数网站都没有公开。
    '''.format(start, update_time, area, average_price[0], price_up_or_low[0] + relative[0], 
            today_new_hosuse_num[0], room_price_up_or_down[0] + room_price_percent[0],today_hosuse_low[0],
            seven_day_nums[3],transfer_lastday[0])

    return content


content = get_content_today()
print(content)
print('*' * 16)
# jinjiang_content = get_content_today(area='锦江区')
# print(jinjiang_content)