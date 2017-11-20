from compare import *
from Examples.Test.features.steps.clientListfile import *

@given(u'I have {name:w} for my user')
def step_impl(context, name):
    context.name = name

@given(u'I have {clientid:d} for my client')
def step_impl(context, clientid):
    context.clientid = clientid

@when(u'I Search {clientid2:d} in the list')
def step_impl(context, clientid2):
    context.clientid2 = clientid2

@then(u'I should receive ${price:d} price of purchase for client')
def step_impl(context, price):
    context.price = price
    id = context.clientid
    dirPrice = Dic.priceList()[id]
    expect(context.price).to_equal(dirPrice)

