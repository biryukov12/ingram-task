from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    def get_paginated_response(self, data):
        content_range = 'items {0}-{1}/{2}'. \
            format(self.offset, self.limit + self.offset - 1, self.count)
        return Response(
            OrderedDict(
                [
                    ('count', self.count),
                    ('next', self.get_next_link()),
                    ('previous', self.get_previous_link()),
                    ('results', data),
                ]
            ),
            headers={'Content-Range': content_range}
        )
