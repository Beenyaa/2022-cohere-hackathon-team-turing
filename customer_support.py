from communication_manager import CommunicationManager


class CustomerSupportChat:
    ...

    def __init__(self, name: str, comm_manager: CommunicationManager) -> None:
        self.name = name
        self._comm_manager = comm_manager

    def send_message(self, msg: str) -> None:
        self._comm_manager.send_message(self.name, msg)


if __name__ == "__main__":
    comm_manager = CommunicationManager()
    c = CustomerSupportChat("Customer Support", comm_manager)

    c.send_message("Hello")
