from abc import ABC, abstractmethod
from find_a_friend.views.http_types.http_request import HttpRequest
from find_a_friend.views.http_types.http_response import HttpResponse


class ViewInterface(ABC):
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pass
