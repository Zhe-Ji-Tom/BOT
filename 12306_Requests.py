import requests
import re


def query():
    query_headers = {
        # 'Connection': 'keep-alive',
        # 'Host': 'kyfw.12306.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        # 'Cache-Control': 'max-age=0',
        # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Sec-Fetch-Dest': 'document',
        # 'Sec-Fetch-Mode': 'navigate',
        # 'Sec-Fetch-Site': 'none',
        # 'Sec-Fetch-User': '?1',
        # 'Upgrade-Insecure-Requests': '1',
    }

    query_data = {
        'leftTicketDTO.train_date': date,
        'leftTicketDTO.from_station': ori,
        'leftTicketDTO.to_station': des,
        'purpose_codes': 'ADULT',
    }

    query_init_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'

    query_url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        query_data['leftTicketDTO.train_date'], query_data['leftTicketDTO.from_station'],
        query_data['leftTicketDTO.to_station'])

    s.get(query_init_url)
    response = s.get(query_url, headers=query_headers)
    response.raise_for_status()
    response.encoding = response.apparent_encoding
    retry = re.search(r'网络(.*)一下', response.text).group(0)


if __name__ == '__main__':
    date = '2020-12-10'
    ori = 'BJP'
    des = "SHH"
    s = requests.session()
    query()
