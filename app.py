import requests

# TODO - So how do i write the code for this?

# ? I'm thinking about taking inputs
# ? So what possible inputs can we take? City and language. Both will be passed in the query param
# ? How -> Run a while loop, the user can exit the while loop if he enters exit
# ? Need to use base_api_url, api_key, as well as requests module
# ! Could be done better, terminal looks stupid

# API_KEY = "9cdbd89bc8944db29ca55552251007"
# BASE_API_URL = rf"http://api.weatherapi.com/v1/current.json"
# terminateLoop = False

# while not terminateLoop:

#     city = input("Enter the city name: ") or "Pune"
#     language = input("Enter the language: ") or "en"
#     params = {"key": API_KEY, "q": city, "lang": language, "aqi": "no"}

#     res = requests.get(
#         BASE_API_URL, params=params
#     )

#     data = res.json()
#     loc = data['location']
#     current = data['current']

#     checkExit = input("Enter any key to continue, enter e to exit ").lower()

#     if checkExit == "e":
#         terminateLoop = True


from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "9cdbd89bc8944db29ca55552251007"
BASE_API_URL = "http://api.weatherapi.com/v1/current.json"


@app.route("/", methods=["GET", "POST"])
def index():
    data = None

    if request.method == "POST":
        city = request.form.get("city")
        language = request.form.get("language", "en")  

        params = {"key": API_KEY, "q": city, "lang": language, "aqi": "no"}

        response = requests.get(BASE_API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
        else:
            data = {
                "error": "Could not fetch weather. Please check the city name."
            }

    return render_template("weather.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
