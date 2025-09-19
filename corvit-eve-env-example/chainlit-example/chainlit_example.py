import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic to process the user's message goes here.
    # For this example, we simply echo the message.

    # Send a response back to the user
    await cl.Message(
        content=f"Received: {message.content}",
    ).send()