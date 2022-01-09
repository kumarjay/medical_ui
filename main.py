from flask import Flask, render_template, request, make_response, jsonify, flash
from flask import redirect, url_for
import json, time, os, glob
import yaml
from send_email import send_mail

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    dept = ['Dental', 'Medicine', 'Orthopedics']
    doctors = ['Anup', 'Jay', 'Vipin']
    phone = '+91 9766135343'
    email = 'ifoxmedia@info.com'
    # pics= ["/home/jay/PycharmProjects/medical_ui/static/img/gallery/gallery-1.jpg",
    #           "static/img/gallery/gallery-2.jpg", "static/img/gallery/gallery-1.jpg",
    #        'static/img/gallery/gallery-1.jpg', "static/img/gallery/gallery-1.jpg"]
    # pics = glob.glob('/home/jay/PycharmProjects/medical_ui/static/img/gallery/*.jpg')
    pics = []
    for files in os.listdir(os.path.join(os.getcwd(), 'static/img/gallery/')):
        pics.append(os.path.join('static/img/gallery', files))
        # print(path)
    return render_template('index.html', department= dept, doctors= doctors, pictures= pics, phone= phone, email= email)


@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    doctor = request.form.get('doctor')
    department = request.form.get('department')
    message = request.form.get('message')
    print('name is :...', name, ' ', date, ' ', department)

    # status = send_mail(name, email, phone, date, doctor, department, message)
    time.sleep(2)
    status =True

    if status == True:
        flash('You appointment is successfully booked !!!')
    else:
        flash('Sorry, There was some technical problem. Please try agian !!')
    return redirect(url_for('index'))
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
