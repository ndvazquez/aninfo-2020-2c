from behave import *
from domain.catalog import Catalog

@given('an item and a Catalog with no items added')
def step_impl(context):
    context.catalog = Catalog(10)
    context.item_name = "Nike Shoes"
    context.item_price = 200

@when('the item is added to the catalog')
def step_impl(context):
    context.catalog.add_item(context.item_name, context.item_price)
    assert context.catalog.find(context.item_name) == context.item_price

@then('the Catalog has one item and no exceptions are raised')
def step_impl(context):
    assert len(context.catalog.items) == 1
