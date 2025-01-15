from celery import shared_task
from ai.agent import SGEAgent


@shared_task
def invoke_sge_agent():
    agent = SGEAgent()
    agent.invoke()
    return 'Agente AI SGE invocado com sucesso.'
