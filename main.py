from flask import Flask
from flask import render_template, request
import time
from interface import create_product, get_product, last
app = Flask(__name__)


@app.route('/manufacturer', methods=['GET', 'POST'])
def manufacturer_page():
    if request.method == "POST":
        timeStamp = str(time.time())
        itemName = request.form["item-name"]
        mfgDate = request.form["manufacturer-date"]
        expiryDate = request.form["expiry-date"]
        batchNo = request.form["batch-number"]
        numberUnits = int(request.form["number-units"])

        create_product(
            timeStamp=timeStamp,
            itemName=itemName,
            mfgDate=mfgDate,
            expiryDate=expiryDate,
            batchNo=batchNo,
            numberUnits=numberUnits
        )
        print(last())

        # print(get_product())

        return render_template('manufacturer.html', submitted=True)

    return render_template('manufacturer.html', submitted=False)


if __name__ == '__main__':
    app.run(debug=True)