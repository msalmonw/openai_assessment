import openai

class ChatGPTChatBot:
    def __init__(self) -> None:
        openai.api_key = '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'
        #initializing prompt for the BOT, which can be improved. This prompt will be used as a context of the whole conversation by appending
        #each user query and its respective response
        self.promptWithContext = [{"role": "system", "content": "Provide answer to user queries in as simple words as possible."}]
        #list of strings for storing the user prompts only 
        self.userPrompts = []

    def createPrompt(self, prompt: str) -> None:
        #add user prompt to the defined userPrompts list
        self.userPrompts.append(prompt)

    def getResponse(self, prompt_index: int) -> str:
        #apeend user prompt at given index to the main context prompt required for Chat Completion
        self.promptWithContext.append({"role": "system", "content": self.userPrompts[prompt_index]})
        #generate response from the API
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.promptWithContext,
            temperature=0.1,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        #get text only from the generated response object by the API
        reply = response["choices"][0]["message"]["content"]
        #append the response to the context prompt
        self.promptWithContext.append({"role": "assistant", "content": reply})
        #return the reply to the user
        return reply
    
    def updatePrompt(self, prompt_index: int, new_prompt: str) -> None:
        #update prompt at given index in the user prompts list
        self.userPrompts[prompt_index] = new_prompt

    def deletePrompt(self, prompt_index: int) -> None:
        #update prompt at given index in the user prompts list
        self.userPrompts.pop(prompt_index)

