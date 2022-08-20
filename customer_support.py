from communication_manager import CommunicationManager


class CustomerSupportChat:
    ...

    def __init__(self, name: str, comm_manager: CommunicationManager) -> None:
        self.name = name
        self._comm_manager = comm_manager

    def send_message(self, msg: str) -> None:
        self._comm_manager.send_message(self.name, msg)

    def recieve_message(self, sender, msg: str) -> None:
        print(f"{sender}: {msg}")



if __name__ == "__main__":
    comm_manager = CommunicationManager()
    c = CustomerSupportChat("Customer Support", comm_manager)
    c.send_message("Hello")
    sender, msg = comm_manager.receive_message()
    c.recieve_message(sender, msg)
