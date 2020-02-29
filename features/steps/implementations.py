from behave import given, when, then
from falcon import testing
from grappa import should

from auth import create


@given("our service is running correctly")
def our_service_is_running_correctly(context):
    context.app = create()
    context.app | should.not_be.equal.to(None)
    context.client = testing.TestClient(context.app)
    context.client | should.not_be.equal.to(None)


@when("the users tries to login with correct credentials")
def login_with_correct_credentials(context):
    context.resp = context.client.simulate_post(
        "/login", json={"username": "correct", "password": "correct"}
    )


@then("the user gets back a token")
def the_user_gets_back_a_token(context):
    with should(context.resp.json):
        should.be.a(dict)
        should.have.key("token").to.be.a(str)


@then('the status code is "{code}"')
def step_impl(context, code):
    context.resp.status_code | should.be.equal.to(int(code))


@when("the users tries to login with incorrect credentials")
def login_incorrect_credentials(context):
    context.resp = context.client.simulate_post(
        "/login", json={"username": "incorrect", "password": "incorrect"}
    )


@then("the user doesn't get back a token")
def user_doesnt_get_back_token(context):
    context.resp.json | should.be.a(dict)
    assert "token" not in context.resp.json
