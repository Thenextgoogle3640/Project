import bs4 
import requests

def getCostcoNamePrice(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.findAll("div", { "class" : "price" })
    elem = soup.findAll("p", { "class" : "description" })
    priced = elems[0].text
    return elem[0].text.strip(),priced[1:]

print(getCostcoNamePrice('https://www.costco.com/CatalogSearch?dept=All&keyword=nutella&pageSize=96'))




# import bs4 
# import requests

# def getCostcoPrice(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#     res = requests.get(url, headers=headers)
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.findAll("div", { "class" : "price" })
#     elems2 = soup.findAll("p", { "class" : "description" })
#     priced = elems[0].text
#     return priced[1:],elems2[0].text.strip()

# itemname = 'nutella'
# c_price, c_name = getCostcoPrice("https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname))

# print(c_name, c_price)

# def getCostcoName(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#     res = requests.get(url, headers=headers)
#     soup = bs4.BeautifulSoup(res.text, 'html.parser')
#     elems = soup.findAll("p", { "class" : "description" })
#     return elems[0].text.strip()


