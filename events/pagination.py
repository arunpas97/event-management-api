from rest_framework.pagination import PageNumberPagination

class AttendeePagination(PageNumberPagination):
    page_size = 10
