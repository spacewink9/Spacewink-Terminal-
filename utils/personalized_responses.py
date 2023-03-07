import json

class PersonalizedResponses:
    def __init__(self, responses_file):
        """
        Initializes the PersonalizedResponses object with a responses file.
        The responses file should be a JSON file with the following format:

        {
            "response_key_1": {
                "text": "The response text for key 1.",
                "variables": {
                    "variable_key_1": "The value for variable key 1.",
                    "variable_key_2": "The value for variable key 2."
                }
            },
            "response_key_2": {
                "text": "The response text for key 2.",
                "variables": {
                    "variable_key_3": "The value for variable key 3.",
                    "variable_key_4": "The value for variable key 4."
                }
            }
            ...
        }

        :param responses_file: The path to the responses file.
        """
        self.responses = {}
        with open(responses_file) as f:
            self.responses = json.load(f)

    def get_response(self, key, variables=None):
        """
        Returns a personalized response based on the given key and variables.

        :param key: The key for the response.
        :param variables: A dictionary of variables to replace in the response text.
        :return: The personalized response text.
        """
        response = self.responses.get(key, None)
        if response is None:
            return f"No response found for key: {key}"

        text = response.get("text", None)
        if text is None:
            return f"No text found for response key: {key}"

        if variables is not None:
            # Replace variables in the response text
            for variable_key, variable_value in variables.items():
                text = text.replace(f"{{{variable_key}}}", str(variable_value))

        return text

    def add_response(self, key, text, variables=None):
        """
        Adds a new response to the responses file.

        :param key: The key for the response.
        :param text: The response text.
        :param variables:
import json

class PersonalizedResponses:
    def __init__(self, responses_file):
        """
        Initializes the personalized responses with the given responses file.
        """
        with open(responses_file) as f:
            self.responses = json.load(f)

    def get_response(self, query):
        """
        Returns a personalized response for the given query, if available.
        """
        for response in self.responses:
            # Check if the query matches any of the personalized response triggers
            if response["trigger"].lower() in query.lower():
                # Replace any placeholders in the response with the corresponding values from the query
                response_text = response["response"].format(**self.extract_placeholders(response["trigger"], query))
                # Return the personalized response
                return response_text

        # No personalized response found for the query
        return None

    def extract_placeholders(self, trigger, query):
        """
        Extracts any placeholders in the trigger and returns a dictionary mapping them to their values in the query.
        """
        placeholders = {}
        # Split the trigger into words
        trigger_words = trigger.split()
        # Split the query into words
        query_words = query.split()
        # Find the index of the trigger words in the query words
        trigger_word_indices = [query_words.index(word) for word in trigger_words if word in query_words]
        # Extract any placeholders in the trigger
        for i, word in enumerate(trigger_words):
            if "{" in word and "}" in word:
                placeholder_name = word.strip("{}")
                placeholders[placeholder_name] = query_words[trigger_word_indices[i]]
        return placeholders
