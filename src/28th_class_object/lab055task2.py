# Task 2
#
# Create a Class Name API - RestfulBooker
#
# name, list_of_api , links {}
#
# print_apis, print_set()

class api:
    def __init__(self, name, list_of_api, links):
        self.name = None
        self.list_of_api = list_of_api
        self.links = links

    def list_of_apis(self):
        print(self.list_of_api)

    def d_links(self):
        print(self.links)
RestfulBooker = api(None,["Api","Rest_api","Soap_api"],{1,2,3,4,5})
RestfulBooker.list_of_apis()
RestfulBooker.d_links()
