import openai

openai.api_key = "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"


class chatGPTController:
    def shoot(self, question):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        chatgpt_responce_text = response["choices"][0]["text"].strip()
        predication = {
            "chatgpt_responce": str(chatgpt_responce_text),
            "From": "Apps_Team_Technologies_PVT_LTD/Research_And_Development_Team",
            "version": "1.0",
            "version_description": "Testing Stage",
        }
        return predication
