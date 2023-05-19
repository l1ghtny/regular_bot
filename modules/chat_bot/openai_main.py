import os
import openai
from dotenv import load_dotenv
from modules.logs_setup import logger

load_dotenv()
openai.organization = "org-dTq0wzkkXgmTQ1GIDabM4fva"
openai.api_key = os.getenv("OPENAI_API_KEY")
model = 'gpt-3.5-turbo'
role = """Ты бот-помощник на дискорд сервере "Зона Дискорда с Саней" (сокращенно - "ЗДС"). Тебя зовут CyberColors. Ты 
умеешь поздравлять с днём рождения и помогать модерации в работе. Саня - автор ютуб-канала "Зона Веселья с Саней" (сокращенно ЗВС) и владелец ЗДС. Денис ARONZ – второй администратор ЗДС, занимается творчеством на YouTube, Twitch, 
Telegram, Boosty. Blackjack – модератор, стример на Twitch. Verlouder – она же Эвелина, Эва, Юрка, она модератор ЗДС и майкрафтер,
рисует, делает видео на YouTube, хочет кофе. Евгений Euclase – модератор и редактор ЗДС, он пишет новости, делает нарезки 
стримов Сани, слушает музыку, слишком много сидит в интернете. Дима MGilbas - модератор ЗДС, он рисует, делает видео 
на YouTube, гейм девит, щитпостит, terminally online. Паша - модератор ЗДС, немного занимается драматургией, любит шутить, всегда готов поддержать. Нейт, он же Артем - модератор ЗДС, увлекается рисованием, слишком много играет в игры."""

logger = logger.logging.getLogger("bot")


def one_response(message):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            temperature=0.4,
            max_tokens=1024,
            messages=[
                {'role': 'system', 'content': role},
                {'role': 'user', 'content': message}
            ]
        )
        logger.info('success')
        reply = response.choices[0]['message']
        content = reply['content']
        tokens_total = response["usage"]["total_tokens"]
    except openai.error.RateLimitError as rate_limited:
        logger.info('rate limited error')
        content = None
        tokens_total = 0
        logger.error(rate_limited)
    except openai.error.APIError as api_error:
        logger.info('bad gateway or similar error')
        logger.error(api_error)
        content = 'OpenAI упал с рандомной ошибкой. Хз, что у них не так, попробуй ещё раз'
        tokens_total = 0
    return content, tokens_total


def multiple_responses(message_list):
    messages = [{'role': 'system', 'content': role}]
    for i in message_list:
        messages.append(i)
    print(messages)
    try:
        response = openai.ChatCompletion.create(
            model=model,
            temperature=0.4,
            max_tokens=1024,
            messages=messages
        )
        logger.info('success')
        reply = response.choices[0]['message']
        content = reply['content']
        tokens_total = response["usage"]["total_tokens"]
    except openai.error.RateLimitError as rate_limited:
        logger.info('rate limited error')
        content = None
        tokens_total = 0
        logger.error(rate_limited)
    except openai.error.APIError as api_error:
        logger.info('bad gateway or similar error')
        logger.error(api_error)
        content = 'OpenAI упал с рандомной ошибкой. Хз, что у них не так, попробуй ещё раз'
        tokens_total = 0
    return content, tokens_total


