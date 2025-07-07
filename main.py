from core.ticket import Ticket


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

