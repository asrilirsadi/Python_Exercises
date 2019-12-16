import math

class PaginationHelper:
    def __init__(self, list, page):
        self.item_list = list
        self.item_per_page = page
        self.len_item = len(self.item_list)
    
    def page_count(self):
        print(int(math.ceil(1.0*(self.len_item/self.item_per_page))))
    
    def item_count(self):
        print(self.len_item)
    
    def page_item_count(self, page_index):
        if (page_index+1) * self.item_per_page <= self.len_item:
            print(self.item_per_page)
        elif page_index*self.item_per_page < self.len_item and (page_index+1)*self.item_per_page>self.len_item:
            print(self.len_item%self.item_per_page)
        else:
            print(-1)
    
    def page_index(self, item_index):
        if item_index < self.len_item and item_index >= 0:
            print(int(math.floor(item_index/self.item_per_page)))
        else:
            print(-1)

helper = PaginationHelper(['a','b','c','d','e','f'],4)
helper.page_count()
helper.item_count()
helper.page_item_count(0)
helper.page_item_count(1)
helper.page_item_count(2)
helper.page_index(5)
helper.page_index(2)
helper.page_index(20)
helper.page_index(-10)