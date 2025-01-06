from django.conf import settings
from openai import OpenAI
from ai import prompts
from products.models import Product
from outflows.models import Outflow
import json
from django.core import serializers
from ai.models import AIResult


class SGEAgent:

    def __init__(self):
        self.__client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
        )

    def __get_data(self):

        products = Product.objects.all()
        outflows = Outflow.objects.all()

        # O json dumps coloca o json -> str
        # E o serializer coloca uma qs -> json.
        return json.dumps({
            'products': serializers.serialize('json', products),
            'outflows': serializers.serialize('json', outflows)
        })

    def invoke(self):
        response = self.__client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=[
                {
                    'role': 'system',
                    'content': prompts.SYSTEM_PROMPT,
                },
                {
                    'role': 'user',
                    'content': prompts.USER_PROMPT.replace(
                        '{{data}}',
                        self.__get_data()
                    ),
                }
            ]
        )

        result = response.choices[0].message.content

        AIResult.objects.create(result=result)
