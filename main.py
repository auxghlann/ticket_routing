from core.ticket import Ticket


user_ticket ="""
                Subject: Urgent - Login Error

                Hi Support Team,

                I'm having trouble accessing my account with the username "example_user." Every time I try to log in, I encounter an error message. I've already attempted to reset my password, but the issue persists. I need to resolve this problem urgently, as I have pending tasks that require immediate attention.

                Please investigate and assist promptly.

                Thanks,
                John.""" 

not_a_ticket = """
                How is the weather today?
                """

if __name__ == "__main__":
    ticket = Ticket()
    chat_completion = ticket.classify_ticket(user_ticket)
    chat_completion2 = ticket.classify_ticket(not_a_ticket)

    print(chat_completion)
    print(chat_completion2)
