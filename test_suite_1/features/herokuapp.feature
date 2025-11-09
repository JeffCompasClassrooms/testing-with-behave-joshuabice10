Feature: Explore the functionality of the herokuapp website
  As a web developer/designer
  I want to explore the functionality
  Of the herokuapp website

  Scenario: Homepage loads successfully
    Given I open the url "https://the-internet.herokuapp.com"
    Then I expect that element "h1" contains the text "Welcome to the-internet"
    Then I expect that element "h2" contains the text "Available Examples"
    Then I expect that element "ul" contains any text
    Then I expect that element "#page-footer" is visible

  Scenario: Notification message link works and a notification message exists.
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/notification_message']"
    Then I expect that element "#flash" is visible
    Then I expect that element "h3" contains the text "Notification Message"

  Scenario: The dropdown link takes you to the dropdown page and dropdown is present
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/dropdown']"
    When I pause for 500ms
    Then I expect the url to contain "/dropdown"
    Then I expect that element "#dropdown" is visible

  Scenario: Key Presses link works and tab selects the textbox
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/key_presses']"
    When I pause for 500ms
    When I press "Tab"
    Then I expect that element "#result" becomes visible

  Scenario: File uploader link works and file uploader button takes you to server error page
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/upload']"
    When I click on the button "input.button"
    When I pause for 500ms
    Then I expect that element "h1" contains the text "Internal Server Error"

  Scenario: Add/Remove Elements link works and the page has an "Add Element" button and a "Delete" button
    Given I open the url "https://the-internet.herokuapp.com/"
    When I click on the element "a[href='/add_remove_elements/']"
    Then I expect that element "button[onclick='addElement()']" is visible
    When I click on the button "button[onclick='addElement()']"
    Then I expect that element "button.added-manually" becomes visible

  Scenario: Mulitple windows link works and the button opens a new tab
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/windows']"
    Then I expect that element "a[href='/windows/new']" is visible
    When I click on the element "a[href='/windows/new']"
    Then I expect the url "https://the-internet.herokuapp.com/windows/new" is opened in a new tab
    Given I open the url "https://the-internet.herokuapp.com/windows/new"
    Then I expect that element "h3" contains the text "New Window"

  Scenario: Checkbox checks and unchecks when clicked on
    Given I open the url "https://the-internet.herokuapp.com/checkboxes"
    When I click on the element "input[type='checkbox']"
    Then I expect that checkbox "input[type='checkbox']" is checked
    When I click on the element "input[type='checkbox']"
    Then I expect that checkbox "input[type='checkbox']" is not checked


  Scenario: Image page link works and has 3 broken broken images
    Given I open the url "https://the-internet.herokuapp.com/"
    When I click on the element "a[href='/broken_images']"
    Then I expect that element "img[src='asdf.jpg']" is visible
    Then I expect that element "img[src='hjkl.jpg']" is visible
    Then I expect that element "img[src='img/avatar-blank.jpg']" is visible

  Scenario: Drag and Drop page has a draggable element
    Given I open the url "https://the-internet.herokuapp.com/drag_and_drop"
    Then I expect that element "div[draggable='true']" is visible
    
