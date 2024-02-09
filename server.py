from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')
@app.route("/index.html")
def my_home2():
    return render_template('index.html')

@app.route("/<page_name>")
def html_page(page_name):
    return (page_name)

@app.route("/generic.html")
def general():
    return render_template('generic.html')
@app.route("/element.html")
def element():
    return render_template('elements.html')

@app.route('/thankyou.html')
def thank():
    return render_template('/thankyou.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["name"]
        subject = data["email"]
        message = data["message"]
        file = database.write(f'{email}, {subject}, {message}\n')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["name"]
        subject = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
   if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
          return 'did not save to database'
   
   else:
      return 'something went wrong. Try again!'