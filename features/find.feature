Feature: Finding an item
  In order to use a catalog for browsing items,
  As a user
  I want to be able to find an item's price in the catalog.

  Scenario: Finding an item's price in the Catalog
     Given an item and a Catalog with such item
      When the item is looked up
      Then the item returned by the Catalog has the correct item's price
