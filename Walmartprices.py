import bs4 
import requests

def getWalmartPrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.findAll("span", { "class" : "Price-characteristic" })
    elem = soup.findAll("span", { "class" : "Price-mantissa" })
    elems2 = soup.findAll("a", { "class" : "product-title-link" })
    whole = elems[0].text
    fraction = elem[0].text
    return whole +"." + fraction, elems2[0].text.strip()

itemname = 'nutella'
w_price, w_name = getWalmartPrice("https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname))

print(w_name, w_price)