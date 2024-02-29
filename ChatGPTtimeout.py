@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith('!chat'):
        # Extract the user's message and obtain a response from ChatGPT
        user_message = message.content[6:].strip()
        gpt_response = chat_with_gpt(user_message)
        await message.channel.send(f'ChatGPT: {gpt_response}')

        # Start a loop to continuously ask the user for new questions until a timeout occurs
        while True:
            try:
                # Receive a new question from the user
                new_question_response = await Bot.wait_for('message', check=lambda m: m.author == message.author and m.channel == message.channel, timeout=20)

                # Send the user's question to ChatGPT and retrieve the response
                new_question = new_question_response.content
                gpt_response = chat_with_gpt(new_question)
                await message.channel.send(f'ChatGPT: {gpt_response}')

            except asyncio.TimeoutError:
                # Exit the loop if a timeout occurs
                break

        # Send a concluding message after the loop ends
        await message.channel.send('Thank you, feel free to ask about any other topic.')

    await Bot.process_commands(message)
