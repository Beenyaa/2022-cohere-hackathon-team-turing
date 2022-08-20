from enum import Enum, auto
from communication_manager import CommunicationManager
from ai_manager import AIManager


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
    def __init__(self, name: str, comm_manager: CommunicationManager, ai_manager: AIManager) -> None:
        self.name = name
        self._comm_manager = comm_manager
        self._ai_manager = ai_manager

    def run(self):
        while True:
            print("Waiting for message...")
            sender, msg = comm_manager.receive_message()

            self.display_message(sender, msg)
            answers = self._ai_manager.answer_message(msg)

            self.display_answers(answers)

            while True:
                select_index = self.choose_message(answers)
                action = self.choose_action()
                terminate = self.handle_action(answers, select_index, action)
                if terminate:
                    break


    def send_message(self, msg: str) -> None:
        self._comm_manager.send_message(self.name, msg)

    def display_message(self, sender, msg: str) -> None:
        print(f"{sender}: {msg}")

    def display_answers(self, msgs: list[str]) -> None:
        print("Answers:")
        for i, m in enumerate(msgs):
            print(f"\t{i+1}: {m}")

    def choose_message(self, msgs: list[str]) -> int:
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

    def handle_action(self, msgs: str, index: int, action: Action) -> bool:
        match action:
            case Action.Edit:
                print(f"Editing ({msgs[index]}): ", end='')
                new_msg = input()
                msgs[index] = new_msg
                for i, m in enumerate(msgs):
                    print(f"\t{i+1}: {m}")
                return False

            case Action.Send:
                self.send_message(msgs[index])
                return True

            case Action.Unselect:
                return True


if __name__ == "__main__":
    comm_manager = CommunicationManager()
    ai_manager = AIManager()
    c = CustomerSupportChat("Customer Support", comm_manager, ai_manager)
    c.run()
