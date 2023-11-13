from flask import Flask, redirect, render_template, request, url_for
import os
import hfpy_utils
import swim_utils

app = Flask(__name__)

# ... (your existing code)


@app.route("/chart/<swimmer_name>/<event>")
def display_chart(swimmer_name, event):
    folder_path = swim_utils.FOLDER
    swimmer_file = f"{swimmer_name}.txt"
    (
        name,
        age,
        distance,
        stroke,
        the_times,
        converts,
        the_average,
    ) = swim_utils.get_swimmers_data(os.path.join(folder_path, swimmer_file))

    the_title = f"{name} (Under {age}) {distance} {stroke}"
    from_max = max(converts) + 50
    the_converts = [hfpy_utils.convert2range(n, 0, from_max, 0, 350) for n in converts]

    the_data = zip(the_converts, the_times)

    return render_template(
        "chart.html",
        title=the_title,
        average=the_average,
        data=the_data,
    )


# ... (your existing code)

if __name__ == "__main__":
    app.run(debug=True)
