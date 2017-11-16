from compare import expect

@given(u'I have connection to "{host}"')
def step_impl(context, host):
    expect(context.host).to_equal(host)
    assert True is True

@when(u'I {method} my request')
def step_impl(context, method):
    expect(context.method).to_equal(method)
    assert True is True

@then(u'I receive status code {code}')
def step_impl(context, code):
    expect(str(context.code)).to_equal(code)
    assert True is True