class CommunicationManager:
    def send_message(self, sender: str, msg: str) -> None:
        print(f"{sender}: {msg}")

    def receive_message(self) -> tuple[str, str]:
        """
        message [name] [msg]
        choices [name] [choice1]|[choice2]|...
        """
        raw_data = input()
        data = raw_data.split(' ')
        if len(data) < 3:
            raise ValueError(f"Failed to parse sender and message from {raw_data}")

        if data[0] == 'message':
            return data[0], data[1], ' '.join(data[2:])

        elif data[0] == 'choices':
            joined_data = ' '.join(data[2:])
            return data[0], data[1], joined_data.split('|')
        
        raise ValueError(f"Failed to parse sender and message from {raw_data}")

    def receive_messages(self) -> tuple[str, list[str]]:
        raw_data = input()
        data = raw_data.split('|')
        if len(data) >= 2:
            return data[0], data[1:]
        
        raise ValueError(f"Failed to parse sender and message from {raw_data}")