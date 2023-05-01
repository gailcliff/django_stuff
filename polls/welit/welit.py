"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from welit_baccend import welit

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    note: str

    def set_text(self, text):
        self.note = text

    def post_note(self):
        new_note_id = welit.add_new_note(note=self.note)
        pc.alert(title=f"New note created: {new_note_id}")


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to CliffNotes!", font_size="2em", color='#F4708F'),
            pc.text_area(placeholder="What's going on?", focus_border_color='purple',
                         on_change=State.set_text, width='700px', height='150px'),
            # pc.link(
            #     "Check out our docs!",
            #     href=docs_url,
            #     border="0.1em solid",
            #     padding="0.5em",
            #     border_radius="0.5em",
            #     _hover={
            #         "color": "rgb(107,99,246)",
            #     },
            # ),
            pc.button(
                "Post to CliffNotes", bg="cornflowerblue", color="white", size="lg", is_full_width=True,
                _hover={
                    "background_color": "#F4708F",
                },
                on_click=State.post_note
            ),
            spacing="1.5em",
            font_size="2em",
            width='700px'
        ),
        padding_top="10%",

    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
