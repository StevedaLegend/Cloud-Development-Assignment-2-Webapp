from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Header, Select

LINES = """I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.""".splitlines()


class SelectApp(App):
    ## CSS_PATH = "select.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        s1 = Select((line, line) for line in LINES)
        yield s1
        self.s2 = Select([(None, None)])
        yield self.s2

 
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.s2.set_options((word, word) for word in str(event.value).split(" "))


if __name__ == "__main__":
    app = Select