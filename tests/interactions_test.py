from pages.interactions_page import SortablePage, SelectablePage


class TestInteractions:
    class TestSortable:

        def test_sortable_list_and_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_and_grid_order('sort_list')
            grid_before, grid_after = sortable_page.change_list_and_grid_order('sort_grid')
            assert list_before != list_after, 'the order of the list has not been changed'
            assert grid_before != grid_after, 'the order of the grid has not been changed'

    class TestSelectable:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
