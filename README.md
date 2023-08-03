 The project has used Python as the preferred programming language. It has also used SQLite for the database and Flask to build the web form.
 First, Download and install the Python installer package. It'll install the PIP package. Next, run a Powershell prompt, then type the following script: 
   pip install sqlite3, Flask, smtplib, random, string
Then create a workspace folder. Name it Patient-Form.
Clone the GitHub repository. The link is: https://github.com/iansmall26/Patient-Form/
Run patients_db.py to create a database.
In the app.py file, change the send email function using your own credentials:
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

Run the Flask app by executing the following command in your terminal: python app.py. If you are running from Visual Code, you can hit the play button on top-right corner.
Once you fill and submit in the form, the output should be this: 
![image](https://github.com/iansmall26/Patient-Form/assets/121866422/a169a6d7-17b4-4823-b646-136279b085bd)
Confirm the email received to look as such:
![image](https://github.com/iansmall26/Patient-Form/assets/121866422/47f746d9-10bd-49ba-a269-cfb6c4e6cf62)
The reference in the output should be the same as the reference in the email body.
