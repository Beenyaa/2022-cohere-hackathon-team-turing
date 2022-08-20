class CommunicationManager:
    def send_message(self, sender: str, msg: str) -> None:
        print(f"{sender}: {msg}")

    def receive_message(self) -> tuple[str, str]:
        raw_data = input()
        data = raw_data.split(' ')
        if len(data) >= 2:
            return data[0], ' '.join(data[1:])
        
        raise ValueError(f"Failed to parse sender and message from {raw_data}")

    def receive_messages(self) -> tuple[str, list[str]]:
        raw_data = input()
        data = raw_data.split('|')
        if len(data) >= 2:
            return data[0], data[1:]
        
        raise ValueError(f"Failed to parse sender and message from {raw_data}")