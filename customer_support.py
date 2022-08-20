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

    def receive_choices(self, sender, msgs: list[str]) -> None:
        print(f"{sender}:")
        for i, m in enumerate(msgs):
            print(f"\t{i+1}: {m}")



if __name__ == "__main__":
    comm_manager = CommunicationManager()
    c = CustomerSupportChat("Customer Support", comm_manager)
    c.send_message("Hello")
    sender, msg = comm_manager.receive_message()
    c.recieve_message(sender, msg)

    sender, msgs = comm_manager.receive_messages()
    c.receive_choices(sender, msgs)