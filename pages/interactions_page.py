import random

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_and_grid_order(self, name_sort):
        sorts = {'sort_list': {'tab': self.locators.TAB_LIST,
                               'items': self.locators.LIST_ITEM},
                 'sort_grid': {'tab': self.locators.TAB_GRID,
                               'items': self.locators.GRID_ITEM}
                 }
        self.element_is_visible(sorts[name_sort]['tab']).click()
        order_before = self.get_sortable_items(sorts[name_sort]['items'])
        item_list = random.sample(self.elements_are_visible(sorts[name_sort]['items']), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(sorts[name_sort]['items'])
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()
