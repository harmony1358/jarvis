import openai
import logging

class Jarvis:

    def __init__(self, key, user, assistant):

        logging.info("Jarvis initializing...");
        
        self.api_key = key
        self.initial_user_prompt = user
        self.initial_assistant_prompt = assistant
        self.conversation = []
        
        self.api_key = key
        self.initial_user_prompt = user
        self.initial_assistant_prompt = assistant

        self.post_init()

    def post_init(self):

        openai.api_key = self.api_key
        self.conversation.append({"role": "user", "content": self.initial_user_prompt})
        self.conversation.append({"role": "assistant", "content": self.initial_assistant_prompt})

        logging.info("Initialized with following prompts: \nuser: " + self.initial_user_prompt
                      + "\nassistant: " + self.initial_assistant_prompt)

    def respond(self, prompt):

        self.conversation.append({"role": "user", "content": prompt});

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )

        response = chat.choices[0].message.content;
        self.conversation.append({"role": "assistant", "content": response});
        return response
    
    def reset(self):
        self.conversation=[]
        self.post_init()
