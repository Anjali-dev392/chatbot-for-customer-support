import random

intents = {
    "intents": [
        {
            "tag": "greeting",
            "patterns": [
                "hello",
                "hi",
                "hey",
                "good morning",
            ],
            "responses": [
                "Hello! How can I help you today?"
            ],
        },
        {
            "tag": "order_tracking",
            "patterns": [
                "where is my order?",
                "track my order",
                "where is my package?",
                "how can i track my delivery?",
            ],
            "responses": [
                "Please provide your order ID to track your package."
            ],
        },
        {
            "tag": "refund",
            "patterns": [
                "how can i get a refund?",
                "i want my money back",
                "how do i request a refund?",
            ],
            "responses": [
                "Please provide your order ID to initiate a refund request."
            ],
        },
    ]
}


def get_response(message):
    text = message.strip().lower()
    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern in text:
                return random.choice(intent["responses"])

    if "order id" in text or "order number" in text:
        return "Thanks. Please share your order ID so I can help you further."

    return "Sorry, I didn't understand that. Can you please rephrase?"
