import json

from falcon import API, status


class LoginResource(object):
    def on_post(self, req, res):
        credentials = json.load(req.bounded_stream)
        if (
            credentials["username"] == "correct"
            and credentials["password"] == "correct"
        ):
            res.media = {"token": "token token super seguro"}
        else:
            res.status = status.HTTP_UNAUTHORIZED
            res.media = {"error": "Invalid credentials"}


def create():
    api = API()
    api.add_route("/login", LoginResource())
    return api
