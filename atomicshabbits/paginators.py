from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = "page_size"
    # can be used as a query parameter to set the page size on a per-request basis.
    max_page_size = 50
    # the maximum allowable requested page size.
