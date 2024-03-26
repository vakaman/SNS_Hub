from src.models import Message
from src import publish
from moto import mock_aws
import boto3


# @mock_aws
# def test_publish_message():
#     sns_client = boto3.client('sns', region_name='us-west-2')
#     topic_arn = sns_client.create_topic(Name='test-topic')['TopicArn']

#     message = Message(
#         {
#             "my": "message",
#             "is": "Hello, world!",
#         }
#     )

#     publish(message, topic_arn)

#     messages = sns_client.list_topic_tags(TopicArn=topic_arn)
#     assert len(messages['Tags']) == 1
#     assert messages['Tags'][0]['Value'] == "Hello, world!"
