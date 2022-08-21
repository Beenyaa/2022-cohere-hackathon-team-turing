import asyncio
from ChatApp.ai_manager import AIManager
from customer_support import CustomerSupportChat


def async_main():
    ai_manager = AIManager('Yz9DQdFfc8L8K0SHUhoMWiurN5R2tkzbGXMLMwRv')
    customer_support = CustomerSupportChat("Customer Support", ai_manager)
    asyncio.run(customer_support.run())


def main():
    async_main()


if __name__ == "__main__":
    main()
