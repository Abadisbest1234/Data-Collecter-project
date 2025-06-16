from flask import Flask, render_template_string, request, redirect, flash
import uuid
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

HTML_FORM = '''
<!doctype html>
<title>User Info Collector</title>
<h2>User Info Collector</h2>
<form method=post>
  First Name: <input name=first_name required><br>
  Last Name: <input name=last_name required><br>
  Age: <input name=age type=number required><br>
  Email: <input name=email type=email required><br>
  Phone Number: <input name=phone required><br>
  Educational Institution (if under 18): <input name=student><br>
  School/Workplace (if 18+): <input name=schoolorwork><br>
  Citizen of Republic of Ireland: <input name=roi required><br>
  Address: <input name=address required><br>
  Continent: <input name=continent required><br>
  Country: <input name=country required><br>
  County: <input name=county required><br>
  <input type=submit value=Submit>
</form>
{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
'''

def send_email(receiver_email, first_name):
    sender_email = "abadisbest1234@gmail.com"
    password = "jwcy vaek pfom rqlu"  # Use an app password for Gmail

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Thank you for your submission!"

    body = f"Hello {first_name},\n\nThank you for submitting your information."
    message.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        FirstName = request.form['first_name']
        LastName = request.form['last_name']
        Age = int(request.form['age'])
        Email = request.form['email']
        PhoneNumber = request.form['phone']
        student = request.form.get('student', '')
        schoolorwork = request.form.get('schoolorwork', '')
        roi = request.form['roi']
        address = request.form['address']
        contanint = request.form['continent']
        country = request.form['country']
        county = request.form['county']

        user_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        with open("user_info.txt", "a") as file:
            file.write(f"User ID: {user_id}\n")
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"First Name: {FirstName}\n")
            file.write(f"Last Name: {LastName}\n")
            file.write(f"Age: {Age} years\n")
            file.write(f"Email: {Email}\n")
            file.write(f"Phone Number: {PhoneNumber}\n")
            if Age < 18:
                file.write(f"Educational Institution: {student}\n")
            else:
                file.write(f"School/Workplace: {schoolorwork}\n")
            file.write(f"Citizen of Republic of Ireland: {roi}\n")
            file.write(f"Address: {address}\n")
            file.write(f"Continent: {contanint}\n")
            file.write(f"Country: {country}\n")
            file.write(f"County: {county}\n")
            file.write("------------------\n")

        send_email(Email, FirstName)
        flash("Information saved and email sent!")
        return redirect('/')

    return render_template_string(HTML_FORM)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)