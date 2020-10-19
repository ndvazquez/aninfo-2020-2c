Feature: Adding
  In order to use a catalog for browsing items,
  As a user
  I want to be able to add items to a catalog.

  Scenario: Adding an item to the Catalog
     Given an item and a Catalog with no items added
      When the item is added to the catalog
      Then the Catalog has one item and no exceptions are raised
