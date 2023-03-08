from flask import Flask
from flask import render_template, request
import time

app = Flask(__name__)

@app.route('/manufacturer',methods=['GET','POST'])
def manufacturer_page():
    if request.method == "POST":
        timeStamp = time.time()
        itemName = request.form["item-name"]
        mfgDate = request.form["manufacturer-date"]
        expiryDate = request.form["expiry-date"]
        batchNo = request.form["batch-number"]
        numberUnits = request.form["number-units"]

        print(itemName)

        return render_template('manufacturer.html',submitted=True)

    return render_template('manufacturer.html',submitted=False)



if __name__ == '__main__':
    app.run(debug=True)