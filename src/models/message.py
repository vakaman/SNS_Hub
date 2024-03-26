import json
import uuid


class Message:

    def __init__(self, content: dict):

        self.content = content

        self._generate_correlation_id()

    def get_content(self):

        return json.dumps(self.content)

    def _generate_correlation_id(self):

        if 'correlation_id' not in self.content:
            self.content['correlation_id'] = str(uuid.uuid4())
            return

        if 'correlation_id' in self.content:
            self._validate_correlation_id(self.content.get('correlation_id'))

    def _validate_correlation_id(self, correlation_id: str):

        if correlation_id is not None:
            try:
                uuid.UUID(correlation_id)
            except ValueError:
                raise ValueError(
                    "Invalid correlation_id: '{}' is not a valid UUID.".format(
                        correlation_id
                    )
                )
