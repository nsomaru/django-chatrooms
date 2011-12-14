from utils.handlers import MessageHandlerFactory  # get_message_received_handler
from django.dispatch import Signal


chat_message_received = Signal(
    providing_args=[
        "room_id",
        "user",
        "message",
        "date",
])

handler = MessageHandlerFactory()

chat_message_received.connect(handler.handle_received_message)