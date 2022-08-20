from communication_manager import CommunicationManager


class ClientChat:
    ...

    def __init__(self, name: str, comm_manager: CommunicationManager) -> None:
        self.name = name
        self.comm_manager = comm_manager

    def send_message(self, msg:str) -> None:
        self.comm_manager.send_message(self.name, msg)
        

    def recieve_message(self, sender:str, msg:str) -> None:
        print(f"{sender}: {msg}")


if __name__ == "__main__":
    comm_manager = CommunicationManager()
    c = ClientChat("Client1", comm_manager)
    c.send_message("Please help me :(")
    sender, msg = comm_manager.receive_message()
    c.recieve_message(sender, msg)
