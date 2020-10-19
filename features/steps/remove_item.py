from behave import *
from domain.catalog import Catalog

@given('an item and a Catalog with such item')
def step_impl(context):
    context.catalog = Catalog(10)
    context.item_name = "Nike Shoes"
    context.item_price = 200
    context.catalog.add_item(context.item_name, context.item_price)
    assert len(context.catalog.items) == 1

@when('the item is removed from the catalog')
def step_impl(context):
    context.catalog.remove_item(context.item_name)

@then('the Catalog no longer has that item and no exceptions are raised')
def step_impl(context):
    assert context.catalog.find(context.item_name) == None
    assert len(context.catalog.items) == 0
