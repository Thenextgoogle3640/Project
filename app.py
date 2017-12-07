from flask import Flask, render_template, request
from Amazonprices import getAmazonNamePrice
from Costcoprices import getCostcoNamePrice
from Walmartprices import getWalmartPrice

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def costco_price():
    if request.method == 'POST':
        itemname = request.form['item']
        curl = "https://www.costco.com/CatalogSearch?dept=All&keyword={itemname}&pageSize=96" .format(itemname=itemname)        
        aurl = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords={itemname}" .format(itemname=itemname)
        wurl = "https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname)

        costconame, costcoinfo = getCostcoNamePrice(curl)
        itemname, iteminfo = getAmazonNamePrice(aurl)
        walmartinfo, walmartname = getWalmartPrice(wurl) 
        if costcoinfo and iteminfo is not None:
            return render_template('results.html', curl = curl, aurl = aurl, wurl = wurl, costconame=costconame, costco_info=costcoinfo, itemname=itemname, item_info=iteminfo, walmartname = walmartname, walmart_info =walmartinfo)
        else:
            return render_template('UI.html', error=True)
    return render_template('UI.html', error=None)




if __name__ == '__main__':
    app.run()