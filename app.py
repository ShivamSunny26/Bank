from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "Sona"

#Database connection
def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user="root",
        password="Shivam@2607",
        database="bank_system"
    )

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/create_account', methods=['GET', 'POST'])
def create_account():
    if request.method == "POST":
        account_number = request.form['account_number']
        account_holder = request.form['account_holder']
        initial_balance = float(request.form['initial_balance'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts (account_number, account_holder, balance) VALUES (%s, %s, %s)",
                       (account_number, account_holder, initial_balance))
        conn.commit()
        cursor.close()
        conn.close()

        flash('Account created Successfully!')
        return redirect(url_for('index'))
    return render_template('create_account.html')

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    if request.method == 'POST':
        account_number = request.form['account_number']
        amount = float(request.form['amount'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Deposit successful!")
        return redirect(url_for('index'))
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == "POST":
        account_number = request.form['account_number']
        amount = float(request.form['amount'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, account_number))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Withdrawal successful!")
        return redirect(url_for('index'))
    return render_template('withdraw.html')

@app.route('/list_accounts')
def list_accounts():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT account_number, account_holder, balance FROM accounts")
    accounts  = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('list_accounts.html', accounts=accounts)

if __name__ == "__main__":
    app.run(debug=True)