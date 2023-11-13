import swim_utils
import hfpy_utils
filename = "Katie-9-100m-Back.txt"
data = swim_utils.get_swimmers_data(filename)
header = """
<!DOCTYPE html>
<html>
    <head>
        <title>
            A simple bar chart
        </title>
    </head>
    <body>
        <h3>A simple bar chart</h3>
"""
print(header)
name, age, distance, stroke, times, values, average = data 
title = f"{data}"

header = f"""
<!DOCTYPE html>
<html>
    <head>
        <title>
            {title}
        </title>
    </head>
    <body>
        <h3>{title}</h3>
"""
print(header)

footer = f""" 
        <p>Average: {average}</p>
    </body>
</html>
"""
print(footer)

body = """ 
        <svg height="30" width="400">
            <rect height="30" width="300" style="fill:rgb(0,0,255);" />
        </svg>Label 1<br />
""" 
print(body)
converts = []
for n in values:
        converts.append(hfpy_utils.convert2range(n, 0, max(values)+50, 0, 400))
times.reverse()
converts.reverse()

body = ""
for t, c in zip(times, converts):
        svg = f""" 
                <svg height="30" width="400">
                        <rect height="30" width="{c}" style="fill:rgb(0,0,255);" />
                </svg>{t}<br />
            """
body = body + svg
print(body)
html = header + body + footer
print(html)
with open("Calvin.html", "w") as df:
        print(html, file=df)