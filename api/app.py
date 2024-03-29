from flask import Flask, render_template
from jinja2 import Template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


# @app.route("/")
# def hello_world():
#     return render_template("first_page.html")


@app.route("/second")
def second_page():
    return render_template("second_page.html")


@app.route("/")
def hello_world():
    return render_template(
        "jinja_intro.html", name="Sam D", template_name="Python and Flask"
    )


@app.route("/expressions/")
def expressions():
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    first_name = "Captain"
    last_name = "Marvel"

    kwargs = {
        "color": color,
        "animal_two": animal_two,
        "animal_one": animal_one,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name,
    }

    return render_template("expressions.html", **kwargs)


@app.route("/fancy")
def hello_world_fancy():
    return """
              <html>
                  <body>
                      <h1>Greetings!</h1>
                      <p>Hello, world!</p>
                  </body>
              </html>
            """


@app.route("/data-structures/")
def data_structures():
    movies = ["Leon the Prof", "The usual suspets", "A beautiful mins"]

    car = {"brand": "Ford", "model": "Fiesta RX", "year": "2018"}

    moons = GalileanMoons("Io", "Europe", "Ganymede", "Callisto")

    kwargs = {"movies": movies, "car": car, "moons": moons}

    # return render_template("data_structures.html", movies=movies, car=car, moons=moons)
    return render_template("data_structures.html", **kwargs)


@app.route("/conditionals/")
def conditionals():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)


@app.route("/for-loops/")
def render_for_loops():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
        "Pluto",
    ]

    return render_template("for_loop.html", planets=planets)


@app.route("/for-loop/conditionals/")
def render_for_loop_conditionals():
    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Sam D": "MacOS",
    }

    return render_template("loops_and_conditionals.html", user_os=user_os)
