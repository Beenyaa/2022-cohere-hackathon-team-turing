from enum import Enum, auto
from communication_manager import CommunicationManager


class Action(Enum):
    Edit = auto()
    Send = auto()
    Unselect = auto()


action_commands = {
    "edit": Action.Edit,
    "send": Action.Send,
    "unselect": Action.Unselect
}


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

    def select_choice(self, msgs: list[str]) -> int:
        index = input()
        if not index.isdigit():
            raise ValueError(f"Could not find message with id: '{index}'")

        index = int(index)
        if not 0 < index <= len(msgs):
            raise ValueError(f"Could not find message number: '{index}'")

        return index-1

    def choose_action(self) -> Action:
        print(f"Choose action: {', '.join(action_commands.keys())}")
        action = input().strip().lower()
        return action_commands[action]

    def handle_action(self, msg: str, action: Action):
        match action:
            case Action.Edit:
                raise NotImplementedError

            case Action.Send:
                print("SENDING")
                raise NotImplementedError

            case Action.Unselect:
                print("UNSELECT")
                raise NotImplementedError


if __name__ == "__main__":
    comm_manager = CommunicationManager()
    c = CustomerSupportChat("Customer Support", comm_manager)
    c.send_message("Hello")
    #sender, msg = comm_manager.receive_message()
    #c.recieve_message(sender, msg)

    sender, msgs = comm_manager.receive_messages()
    c.receive_choices(sender, msgs)

    msg_index = c.select_choice(msgs)
    print(msgs[msg_index])

    action = c.choose_action()
    c.handle_action(msgs[msg_index], action)