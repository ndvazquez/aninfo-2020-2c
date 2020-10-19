from behave import *
from domain.catalog import Catalog

@given('an item and a Catalog with a pair of Nikes')
def step_impl(context):
    context.catalog = Catalog(10)
    context.item_name = "Nike Shoes"
    context.item_price = 200
    context.catalog.add_item(context.item_name, context.item_price)
    assert len(context.catalog.items) == 1

@when('the item is looked up')
def step_impl(context):
    context.found_item_price = context.catalog.find(context.item_name)

@then('the item returned by the Catalog has the correct item\'s price')
def step_impl(context):
    assert context.found_item_price == context.item_price