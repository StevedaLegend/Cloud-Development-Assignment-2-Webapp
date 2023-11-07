#Import the required modules
import os
import webbrowser
import swim_utils
import hfpy_utils
filename = "Darius-13-100m-Fly.txt"
data = swim_utils.get_swimmers_data(filename)
#Using pip install textual we install textual and use from to get the module we need
from rich.text import Text
from rich import print
from rich.console import Console
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Label, Select



#Create a new string object from the given object. 
class SwimmersApp(App[str]):

    
    #State the CSS PATH for the textual 
    CSS_PATH = "Swimmingdata.tcss"

    #Defines the method on_load created method with a title
    def on_load(self):
        self._title = "Swimmers Data"

    #Defines the method where we get the string of the file name and splits it from -
    def get_displayed_name(self, file_name: str) -> str:
        parts = file_name.split("-")
        if len(parts) >= 2:
            return parts[0].capitalize()
        else:
            return file_name

    #files_for_selected_swimmer = allSwimmersFiles(selected_swimmer)

    #Defines the header and label as imported from textual
    def compose(self) -> ComposeResult: 
        yield Header()
        yield Label("Click to go to Swimmers Data", id="Swimmer")

        #Finds the directory path to the swimdata and sees if it ends with .txt
        directory_path = "C:\\Users\\denis\\Downloads\\Cloud Development Assignment\\swimdata"
        txt_files = [file for file in os.listdir(directory_path) if file.endswith(".txt")]

        #Senses the displayed file_name and sets it as the first name
        unique_names = set(self.get_displayed_name(file_name) for file_name in txt_files)


        options1 = [(name, name) for name in unique_names]

        select_widget1 = Select(
            options=options1,
            prompt="Select a swimmer",
            allow_blank=True,
            value=None,
        )

        yield select_widget1

        
        # Display the label at the top of the second Select widget
        yield Label("Click to go to Events Data", id="EventsLabel")

        # Use the selected swimmer to populate the options for the second Select widget
        self.s2 = Select([(None, None)], id="events2")
        yield self.s2

        #Do you wish to continue button
        yield Label("Do you wish to continue?")
        yield Button("Yes", id="yes_button")
        yield Button("No", id="no_button")
    
    #@on selects the event and if the file name ends in txt it associcates with the file that has the name at the start
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        filenamelist1 = []
        for file_name in os.listdir("C:\\Users\\denis\\Downloads\\Cloud Development Assignment\\swimdata"):
            if file_name.endswith(".txt"):
                if event.value in file_name:
                     filenamelist1.append((file_name, file_name))
        self.s2.set_options(filenamelist1)

        # Check if the selected item is an event (ends with .txt) if so it then prints the chart
        if event.value.endswith(".txt"):
            selected_file = event.value
            data = swim_utils.get_swimmers_data(selected_file)
            self.swimmerbarchart(data)

            # Open the HTML file
            urlwebpage = 'Calvin.html'
            webbrowser.open_new_tab(urlwebpage)
            webbrowser.open_new(urlwebpage)
        
    


    #Defines the bar chart in html 
    def swimmerbarchart(self, data):
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
    app = SwimmersApp()
    reply = app.run()
    print(reply)
