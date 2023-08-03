from flask import Flask, render_template, request
import sqlite3
import smtplib
import random
import string

app = Flask(__name__)

# Generate a random patient reference number
def generate_reference_number():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(6))

# Save patient details to the database
def save_to_database(data):
    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO patients (name, dob, email, phnumber, id_number, address, county, sub_county, gender, marital_status,
                                           next_of_kin_name, next_of_kin_dob, next_of_kin_id_number, next_of_kin_gender, next_of_kin_relationship, next_of_kin_phnumber)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (data['name'], data['dob'], data['id_number'], data['email'], data['phnumber'], data['address'], data['county'], data['sub_county'],
                    data['gender'], data['marital_status'], data['next_of_kin_name'], data['next_of_kin_dob'],
                    data['next_of_kin_id_number'], data['next_of_kin_gender'], data['next_of_kin_relationship'], data['next_of_kin_phnumber'],))
    conn.commit()
    conn.close()

# Send email to the patient
def send_email(email, reference_number):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'mungaiiankamau@gmail.com'
    sender_password = 'cdpoxboxmfzwjrgm'

    subject = 'Patient Registration Successful'
    body = f'Dear Patient,\n\nYour registration is successful. Your reference number is: {reference_number}\n\nThank you.'

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message)

@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        reference_number = generate_reference_number()
        save_to_database(data)
        send_email(data['email'], reference_number)
        return f"Registration successful. Your reference number: {reference_number}"
    return render_template('registration_form.html')

if __name__ == '__main__':
    app.run(debug=True)
