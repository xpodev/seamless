from pathlib import Path
from dataclasses import dataclass
from json import load
from seamless import Div, Component, Img

HERE = Path(__file__).parent

users = load((HERE / "users.json").open(encoding="utf-8"))


@dataclass
class UserPage(Component):
    user_id: int

    def render(self):
        if self.user_id >= len(users):
            return Div(classes="container")(
                Div(classes="row")(
                    Div(classes="display-1 text-center")("User not found"),
                )
            )

        user = users[self.user_id]
        user_name = (
            f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
        )

        return Div(classes="container")(
            Div(classes="row")(
                Div(classes="text-center")(
                    Img(
                        src=user["picture"]["large"],
                        alt=user_name,
                        classes="rounded-circle",
                    ),
                ),
                Div(classes="display-1 text-center")(user_name),
                Div(classes="display-6 text-center")(f"Email: {user['email']}"),
            ),
        )
