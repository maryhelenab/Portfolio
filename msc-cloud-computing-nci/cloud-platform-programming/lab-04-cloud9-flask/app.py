from flask import Flask, render_template, request
# flask creates the web app
#render_template loads HTML pages
#request reads user input

app = Flask(__name__) #Tells Flask where the main file is.
 
names = ["Aline","Bob", "Charlie"] #List of users that will appear on the home page.

@app.route("/")
def home():
	return render_template("home.html", names=names) #Displays HTML file / Sends names list

@app.route("/user/<username>") #If user visits:/user/Alice -> Flask understands: username = "Alice"
def profile(username):
	return render_template("profile.html", username=username) #Shows page with personalized name.

@app.route("/login", methods=["GET", "POST"]) #This route accepts two methods.
# Get = Show form or Post = send data
def login():
	if request.method == "POST":
		username = request.form["username"] # Gets the name typed in the form.
		return render_template("success.html", username=username) # Shows page with submitted name.
	return render_template("Login.html") #If user just opened /login, it shows the form.

if __name__ =="__main__":
	app.run(debug=True) #Starts the server.
#debug=True means: auto reload and shows error messages
