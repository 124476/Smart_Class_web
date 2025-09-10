from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50  # Уменьшите для мобильных
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        # Убедимся, что queryset ordered
        if not queryset.ordered:
            queryset = queryset.order_by('id')
        return super().paginate_queryset(queryset, request, view)