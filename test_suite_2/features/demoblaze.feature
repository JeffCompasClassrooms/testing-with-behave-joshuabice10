Feature: Explore the functionality of the herokuapp website
  As a web developer/designer
  I want to explore the functionality
  Of the herokuapp website

  Scenario: Homepage loads successfully
    Given I am on the Demoblaze homepage
    Then I should see the logo and store name
    Then I should see a functioning carousel
    Then I should see all the categories
    Then I should see nine products on the page
  
  Scenario: Signup and login is successful
    Given I am on the Demoblaze homepage
    When I sign up with a valid username and password
    When I login with my created username and password
    Then I should see my username displayed in the navbar

  Scenario: Categories correctly sort their products
    Given I am on the Demoblaze homepage
    When I click on the phones category
    Then I should see seven phones
    When I click on the laptop category
    Then I should see six laptops
    When I click on the monitors category
    Then I should see two monitors
    When I click on the categories button
    Then I should see all the categories

  Scenario: I can click on a product and add it to the cart
    Given I am on the Demoblaze homepage
    When I click on the Samsung galaxy s6
    Then I should see the correct product
    When I click on add samsung to cart
    Then I should see a product added alert

  Scenario: I can delete a product from the cart
    Given I am on the Demoblaze homepage
    When I click on the cart page
    Then I should see the phone in my cart
    When I click the delete button in my cart
    Then I won't see my item in my cart anymore

  Scenario: I can submit a contact message
    Given I am on the Demoblaze homepage
    When I click on the contact nav button
    Then I should see the new message modal
    When I click send message
    Then I see the alert pops up

  Scenario: I can view the about us modal
    Given I am on the Demoblaze homepage
    When I click on about us nav button
    Then I should see the about us modal
    When I click close
    Then I shouldn't see the about us modal

  Scenario: The home button should bring me to the main page
    Given I am on the Demoblaze homepage
    When I click on the cart page
    Then I should be on the cart page
    When I click on the home button
    Then I should be on the home page

Scenario: The next button shows me more products
    Given I am on the Demoblaze homepage
    Then I should see nine products on the page
    When I click the next button
    Then I should see six products on the page

Scenario: I cannot purchase my cart without entering the required info
    Given I am on the Demoblaze homepage
    When I click on the cart page
    When I click on place order
    Then I should see the place order modal
    When I click on the purchase button
    Then I see the alert pops up

Scenario: I can purchase successfully when I fill out the info
    Given I am on the Demoblaze homepage
    When I click on the cart page
    When I click on place order
    Then I should see the place order modal
    When I enter all the required information
    When I click on the purchase button
    Then I see the thank you message

Scenario: I can add multiple products to the same cart
    Given I am on the Demoblaze homepage
    When I click on the Samsung galaxy s6
    When I click on add samsung to cart
    Then I see the alert pops up
    When I click on the home button
    When I click on the Nexus 6
    When I click on add nexus to cart
    Then I see the alert pops up
    When I click on the cart page
    Then I should see all products listed

Scenario: I can logout but stay on the site
    Given I am on the Demoblaze homepage
    When I click logout
    Then I should no longer be logged in

Scenario: I can add orders to my cart even when logged out
    Given I am on the Demoblaze homepage
    When I click on the Samsung galaxy s6
    When I click on add samsung to cart
    Then I see the alert pops up
    When I click on the home button
    When I click on the Nexus 6
    When I click on add nexus to cart
    Then I see the alert pops up
    When I click on the cart page
    Then I should see all products listed

Scenario: I can order a product even when logged out
    Given I am on the Demoblaze homepage
    When I click on the Samsung galaxy s6
    When I click on add samsung to cart
    Then I see the alert pops up
    When I click on the cart page
    When I click on place order
    Then I should see the place order modal
    When I enter all the required information
    When I click on the purchase button
    Then I see the thank you message

    