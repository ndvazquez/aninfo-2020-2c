Feature: Removing
  In order to use a catalog for browsing items,
  As a user
  I want to be able to remove items from a catalog.

  Scenario: Removing an item from the Catalog
     Given an item and a Catalog with such item
      When the item is removed from the catalog
      Then the Catalog no longer has that item and no exceptions are raised
