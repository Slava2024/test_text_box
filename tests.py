from text_box_page import SearchLocators, SearchOutputLocators, SearchText

def test_box_text(browser):
    main_page = SearchText(browser)
    main_page.go_to_site()
    
    user_name = main_page.enter_word(SearchLocators.LOCATOR_USER_NAME, "full_name")
    permanent_address = main_page.enter_word(SearchLocators.LOCATOR_PERMANENT_ADDRESS, "permanent_address")
    current_address = main_page.enter_word(SearchLocators.LOCATOR_USER_CURRENT_ADDRESS, "current_address")
    user_email = main_page.enter_word(SearchLocators.LOCATOR_USER_EMAIL, "email")
    
    main_page.click_on_the_search_button()
    
    user_name_output = main_page.search_word(SearchOutputLocators.LOCATOR_USER_NAME)
    user_email_output = main_page.search_word(SearchOutputLocators.LOCATOR_USER_EMAIL)
    permanent_address_output = main_page.search_word(SearchOutputLocators.LOCATOR_PERMANENT_ADDRESS)
    current_address_output = main_page.search_word(SearchOutputLocators.LOCATOR_USER_CURRENT_ADDRESS)
    
    assert user_name == user_name_output
    assert user_email == user_email_output
    assert permanent_address == permanent_address_output
    assert current_address == current_address_output
    
    
