import bs4
import requests

def getAmazonNamePrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.findAll("span", { "class" : "a-offscreen" })
    price = elems[0].text
    elem = soup.findAll({"h2" : "data-attribute"})
    return elem[13].text,price[1:]

print(getAmazonNamePrice('https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords=nutella'))


# import bs4
# import requests

# def getAmazonPrice(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#     res = requests.get(url, headers=headers)
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.findAll("span", { "class" : "a-offscreen" })
#     price = elems[0].text
#     return price[1:]

# def getAmazonName(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#     res = requests.get(url, headers=headers)
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.findAll({"h2" : "data-attribute"})
#     return elems[0].text


# itemname = 'nutella'
# w_price, w_name = getAmazonPrice("https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname))

# print(w_name, w_price)