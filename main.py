import os
import argparse
from chatbot import Chatbot
from recommendation_engine import RecommendationEngine
from feedback import FeedbackHandler

# Set up command line arguments
parser = argparse.ArgumentParser(description='AI Chatbot')
parser.add_argument('--name', type=str, default='AI Bot',
                    help='Name of the chatbot (default: AI Bot)')
parser.add_argument('--language', type=str, default='en',
                    help='Language of the chatbot (default: en)')
parser.add_argument('--recommendations', action='store_true', default=False,
                    help='Enable recommendation engine')
parser.add_argument('--feedback', action='store_true', default=False,
                    help='Enable feedback mechanism')

# Parse command line arguments
args = parser.parse_args()

# Initialize chatbot
chatbot = Chatbot(args.name, args.language)

# Initialize recommendation engine (if enabled)
if args.recommendations:
    recommendation_engine = RecommendationEngine()
    chatbot.set_recommendation_engine(recommendation_engine)

# Initialize feedback handler (if enabled)
if args.feedback:
    feedback_handler = FeedbackHandler()
    chatbot.set_feedback_handler(feedback_handler)

# Main loop for chatbot
while True:
    # Get user input
    user_input = input('> ')

    # Exit if user types 'exit'
    if user_input == 'exit':
        break

    # Get chatbot response
    response = chatbot.get_response(user_input)

    # Print chatbot response
    print(response)
