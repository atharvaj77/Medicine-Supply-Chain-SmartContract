from flask import Flask
from flask import render_template, request
import time
from interface import create_product, get_product, call_chutiya


app = Flask(__name__)

@app.route('/manufacturer',methods=['GET','POST'])
def manufacturer_page():
    if request.method == "POST":
        timeStamp = str(time.time())
        itemName = request.form["item-name"]
        mfgDate = request.form["manufacturer-date"]
        expiryDate = request.form["expiry-date"]
        batchNo = request.form["batch-number"]
        numberUnits = int(request.form["number-units"])

        
        productId = create_product(
            timeStamp=timeStamp,
            itemName=itemName,
            mfgDate=mfgDate,
            expiryDate=expiryDate,
            batchNo=batchNo,
            numberUnits=numberUnits
        )
        print(productId)

        productData = get_product(productId=productId)
        print(productData)

        return render_template('manufacturer.html',submitted=True)

    return render_template('manufacturer.html',submitted=False)



if __name__ == '__main__':
    app.run(debug=True)