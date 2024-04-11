from behave import *
from selenium.common import NoAlertPresentException

from features.pages.CartPage import CartPage
from features.pages.HomePage import HomePage
from features.pages.ItemPage import ItemPage
from features.pages.PhonesPage import PhonesPage
from features.pages.PlaceOrderPage import PlaceOrderPage


@given(u'Navigate to home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.select_phone_category()


@when(u'Select a phone')
def step_impl(context):
    context.phones_page = PhonesPage(context.driver)
    context.phones_page.select_an_item()


@when(u'Add the phone to cart')
def step_impl(context):
    context.item_page = ItemPage(context.driver)
    context.item_page.add_to_cart()


@when(u'Navigate to cart')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    try:
        context.item_page.accept_alert()
    except NoAlertPresentException:
        print("No alert present.")
    context.home_page.navigate_to_cart()


@then(u'Item should be available in the cart')
def step_impl(context):
    context.cart_page.item_availability()


@given(u'Navigate to cart')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.navigate_to_cart()


@when(u'Select Place Order')
def step_impl(context):
    context.cart_page = CartPage(context.driver)
    context.cart_page.select_place_order()


@when(u'Enter the details')
def step_impl(context):
    context.place_order_page = PlaceOrderPage(context.driver)
    for row in context.table:
        context.place_order_page.enter_name(row["name"])
        context.place_order_page.enter_country(row["country"])
        context.place_order_page.enter_city(row["city"])
        context.place_order_page.enter_credit_card(row["credit_card"])
        context.place_order_page.enter_month(row["month"])
        context.place_order_page.enter_year(row["year"])
    # context.place_order_page.enter_name("Ash")
    # context.place_order_page.enter_country("India")
    # context.place_order_page.enter_city("Tvm")
    # context.place_order_page.enter_credit_card("aaa")
    # context.place_order_page.enter_month("Apr")
    # context.place_order_page.enter_year("2024")


@when(u'Select purchase')
def step_impl(context):
    context.place_order_page.click_on_purchase()


@then(u'Shows Confirmation')
def step_impl(context):
    context.place_order_page.accept_pop_up()
