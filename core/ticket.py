import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

class Ticket:

    SYSTEM_PROMPT = """You are a helpful assistant that classifies support tickets into categories such as technical issues, billing inquiries, or product feedback."""

    def classify_ticket(self, prompt):
        """
        Function to classify support tickets into categories such as technical issues, billing inquiries, or product feedback.
        """
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": Ticket.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": """Classify the ticket delimited in triple backticks if it is a technical issue, 
                                    billing inquiry, or product feedback. and I want you to follow this format:

                                    Ticket: ticket
                                    Classification: [Technical Issue, Billing Inquiry, Product Feedback]

                                    Classify the following ticket:
                                    ticket: ```I am having trouble logging into my account. 
                                    I keep getting an error message that says 'Invalid credentials'. 
                                    I have tried resetting my password but it still doesn't work. Can you help me with this?```
                                """
                },
                {
                    "role": "assistant",
                    "content": """{
                                    "Ticket": "I am having trouble logging into my account. 
                                    I keep getting an error message that says 'Invalid credentials'. 
                                    I have tried resetting my password but it still doesn't work. Can you help me with this?",
                                    "Classification": ["technical issue"]
                                """
                },

                {
                    "role": "user",
                    "content": f"Classify the following ticket: ```{prompt}```"
                }
            ],
            max_tokens=500,
            model="deepseek-r1-distill-llama-70b"
        )
        return response.choices[0].message.content






if __name__ == "__main__":
    ticket = Ticket()
    chat_completion = ticket.classify_ticket("""
                                            Subject: Urgent - Login Error

                                            Hi Support Team,

                                            I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.

                                            Please investigate and assist promptly.

                                            Thanks,
                                            John.""")

    print(chat_completion)
