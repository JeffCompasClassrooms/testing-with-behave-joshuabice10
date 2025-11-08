Feature: Find out if it's Christmas or not
  As a person of celebration
  I want to know if it's Christmas
  So that I don't forget to celebrate.

  Scenario: Homepage loads successfully
    Given I open the url "https://the-internet.herokuapp.com"
    Then I expect that element "h1" contains the text "Welcome to the-internet"

  Scenario: There is a dropdown link on the-internet
    Given I open the url "https://the-internet.herokuapp.com"
    Then I expect that element "a[href='/dropdown']" contains the text "Dropdown"

  Scenario: The dropdown link takes you to the dropdown page
    Given I open the url "https://the-internet.herokuapp.com"
    When I click on the element "a[href='/dropdown']"
    Then I expect the url to contain "/dropdown"

  Scenario: Dropdown element is present
    Given I open the url "https://the-internet.herokuapp.com/dropdown"
    Then I expect that element "#dropdown" is visible

  Scenario: File uploader button takes you to server error page
    Given I open the url "https://the-internet.herokuapp.com/upload"
    When I click on the button "input.button"
    When I pause for 1000ms
    Then I expect that element "h1" contains the text "Internal Server Error"

  Scenario: Add/Remove Elements page has Add button
    Given I open the url "https://the-internet.herokuapp.com/add_remove_elements/"
    Then I expect that element "button" is visible

  Scenario: Infinite scroll text is present
    Given I open the url "https://the-internet.herokuapp.com/infinite_scroll"
    Then I expect that element "div.jscroll-added" is visible

  Scenario: Checkbox checks when clicked on
    Given I open the url "https://the-internet.herokuapp.com/checkboxes"
    When I click on the element "input[type='checkbox']"
    Then I expect that checkbox "input[type='checkbox']" is checked


  Scenario: Image page has blank avatar image
    Given I open the url "https://the-internet.herokuapp.com/broken_images"
    Then I expect that element "img[src='img/avatar-blank.jpg']" is visible

  Scenario: Drag and Drop page has a draggable element
    Given I open the url "https://the-internet.herokuapp.com/drag_and_drop"
    Then I expect that element "div[draggable='true']" is visible
    
