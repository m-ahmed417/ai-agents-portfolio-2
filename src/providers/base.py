from abc import ABC, abstractmethod
from src.schemas import TicketRoute

class BaseTriageProvider(ABC):
    @abstractmethod
    def route_ticket(self, message:str) -> TicketRoute:
        pass
    