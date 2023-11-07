import os
import webbrowser
import swim_utils
import hfpy_utils
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select, Label, Button
from rich.text import Text

class SelectApp(App[str]):
    CSS_PATH = "Swimmingdata.tcss"

    def on_load(self):
        self._title = "Swimmers Data"

    def file_swimmer_name(self, file_name: str) -> str:
        parts = file_name.split("-")
        if len(parts) >= 2:
            return parts[0].capitalize()
        else:
            return file_name

    def get_event_swimmer(self, swimmer_name, directory_path):
        swimmer_events = []
        for file_name in os.listdir(directory_path):
            if file_name.startswith(swimmer_name):
                swimmer_events.append(file_name)
        return swimmer_events

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Enter the swimmer")

        directory_path = "C:\\Users\\denis\\Downloads\\Cloud Development Assignment\\swimdata"
        txt_files = [file for file in os.listdir(directory_path) if file.endswith(".txt")]
        uni_name = set(self.file_swimmer_name(file_name) for file_name in txt_files)

        option2 = [(name, name) for name in uni_name]

        select_one = Select(
            options=option2,
            prompt="Enter the swimmer",
            allow_blank=True,
            value=None,
        )

        yield select_one

        yield Label("click to go Data")

        self.s1 = Select([(None, None)])
        yield self.s1

    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        filenamelist = []
        for file_name in os.listdir("C:\\Users\\denis\\Downloads\\Cloud Development Assignment\\swimdata"):
            if file_name.endswith(".txt"):
                if event.value in file_name:
                    filenamelist.append((file_name, file_name))
        self.s1.set_options(filenamelist)

        filename = event.value
        data = swim_utils.get_swimmers_data(filename)

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

if __name__ == "__main__":
    app = SelectApp()
    app.run()
