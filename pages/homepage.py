class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://sneakdoc.com"

        # Locators
        self.shop_now_button = page.get_by_role("link", name="Shop Now").first
        self.all_products_link = page.get_by_role("link", name="ALL PRODUCTS")
        self.sign_up_button = page.get_by_text("SIGN-UP")
        self.cart_link = page.get_by_text("VIEW CART")
        self.chatbot_icon = page.locator("div[class*='chat'], div[id*='chat']")

    def goto(self):
        self.page.goto(self.url)

    def click_shop_now(self):
        self.shop_now_button.click(force=True)
        self.page.wait_for_load_state("networkidle")

    def click_all_products(self):
        self.all_products_link.click()

    def open_chatbot(self):
        self.chatbot_icon.first.click()