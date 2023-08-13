from flask import Flask, request, jsonify
from openAiBot import ChatGPTChatBot

class ChatBotAPI:
    def __init__(self) -> None:
        self.chatBot = ChatGPTChatBot()

    def startApp(self):
        app = Flask(__name__)

        @app.route('/prompt', methods=['POST'])
        def prompt():
            prompt = request.json['prompt']
            self.chatBot.createPrompt(prompt)
            return "You Entered: " + self.chatBot.userPrompts[len(self.chatBot.userPrompts) - 1]

        @app.route('/response', methods=['POST'])
        def response():
            index = request.json['index']
            reply = self.chatBot.getResponse(index)
            return reply

        @app.route('/update', methods=['POST'])
        def update():
            index = request.json['index']
            prompt = request.json['prompt']
            self.chatBot.updatePrompt(prompt_index=index, new_prompt=prompt)
            return "Prompt updated to: " + self.chatBot.userPrompts[index]
        
        @app.route('/delete', methods=['POST'])
        def delete():
            index = request.json['index']
            self.chatBot.deletePrompt(index)
            return "Prompt deleted at Index " + str(index)
        
        app.run()


if __name__ == '__main__':
    api = ChatBotAPI()
    api.startApp()