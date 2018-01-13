start = 0
url = 'https://movie.douban.com/top250?start='

ends = '&filter='
start_urls = [url + str(start) + ends]
print(start_urls)