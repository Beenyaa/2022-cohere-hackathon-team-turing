import asyncio
from ai_manager import AIManager
from customer_support import CustomerSupportChat


def async_main():
    ai_manager = AIManager()
    customer_support = CustomerSupportChat("Customer Support", ai_manager)
    asyncio.run(customer_support.run())

    """
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)

    routines = [
        customer_support.run()
    ]
    try:
        event_loop.run_until_complete(asyncio.gather(*routines))
    except DeprecationWarning:
        ...
    """

def main():
    async_main()

if __name__ == "__main__":
    main()