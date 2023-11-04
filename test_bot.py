'''import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']

app = App(token=SLACK_BOT_TOKEN)
def log_request(logger, body, next):
    logger.debug(body)
    next()
    


@app.message("hey chatbot")
def send_hello_message(message, say):
    # print(message)
    say(
        text=f"<@{message['user']}> please submit your daily standup.",
        blocks=[
            {
                "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<@{message['user']}> please submit your daily standup."
                        }
            },
            {
                "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "style": "primary",
                                "text": {
                                        "type": "plain_text",
                                        "text": "Submit Report"
                                },
                                "value": "click_me_123",
                                "action_id": "submit_standup"
                            }
                        ]
            }
        ]
    )

if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()
    '''

import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
#import mysql.connector

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
'''MYSQL_USERNAME = os.environ['MYSQL_USERNAME']
MYSQL_PASSWORD = os.environ['MYSQL_PASSWORD']



# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="your_db_user",
    password="your_db_password",
    database="your_db_name"
)

# Create a cursor object
cursor = mydb.cursor()

cursor.execute(
    
    CREATE TABLE IF NOT EXISTS standup_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    user_name VARCHAR(255) NOT NULL,
    yesterday_report TEXT,
    today_plan TEXT,
    blockers TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

    '''


app = App(token=SLACK_BOT_TOKEN)


def log_request(logger, body, next):
    logger.debug(body)
    next()

@app.message("hey chatbot")
def send_hello_message(message, say):
    # print(message)
    say(
        text=f"<@{message['user']}> please submit your daily standup.",
        blocks=[
            {
                "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<@{message['user']}> please submit your daily standup."
                        }
            },
            {
                "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "style": "primary",
                                "text": {
                                        "type": "plain_text",
                                        "text": "Submit Report"
                                },
                                "value": "click_me_123",
                                "action_id": "submit_standup"
                            }
                        ]
            }
        ]
    )

@app.command("/standup")
def create_standup(ack, body, logger, client):
    ack()
    try:
        response = client.views_open(
            trigger_id=body["trigger_id"],
            view={

                "type": "modal",
                "title": {
                        "type": "plain_text",
                        "text": "Standup Bot"
                },
                "submit": {
                    "type": "plain_text",
                    "text": "Submit Standup",
                    "emoji": True
                },
                "close": {
                    "type": "plain_text",
                    "text": "Cancel",
                    "emoji": True
                },
                "callback_id": "submit_your_standup",
                "clear_on_close": True,
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                                "type": "plain_text",
                                "text": "Kindly update your standup.",
                                "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "multiline": True,
                                "action_id": "plain_text_input-action-y"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "What will you do today?",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "multiline": True,
                                "action_id": "plain_text_input-action-t"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "What you did yesterday?",
                            "emoji": True
                        }
                    },
                    {
                        "type": "input",
                        "element": {
                                "type": "plain_text_input",
                                "action_id": "plain_text_input-action-b"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Any Blockers?",
                            "emoji": True
                        }
                    }
                ]

            }
        )
        logger.info(response)

    except SlackApiError as e:
        logger.error("Error creating conversation: {}".format(e))


@app.view('submit_your_standup')
def submit_standup(body, ack):
    ack()
    standup_data = []

    # Username and UserID
    user_id = body['user']['id']
    user_name = body['user']['username']
    # Standup Data
    standup_dataset = body['view']['state']['values']

    standup_data.append(user_id)
    standup_data.append(user_name)

    for data in standup_dataset:
        for data_id in standup_dataset[data]:
            standup_data.append(standup_dataset[data][data_id]['value'])

    print(standup_data)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()