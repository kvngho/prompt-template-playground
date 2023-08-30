from typing import List

import requests
from bs4 import BeautifulSoup
from textrankr import TextRank

from settings import TOKENIZER_CLASSES
from langchain import OpenAI, PromptTemplate

def get_tokenizer(tokenizer_name):
    tokenizer_dict = {
        instance.Meta.name: instance for instance in TOKENIZER_CLASSES
    }
    return tokenizer_dict[tokenizer_name]()


def get_prompt(prompt_template, content):
    prompt_template = PromptTemplate.from_template(prompt_template)
    return prompt_template.format(content=content)

class PlayGround:
    api_key: str
    crawl_data: str
    prompt_template: str
    crawl_result: str
    urls: str
    number_of_sentences: int
    tokenizer_name: str
    summary: str
    prompt: str
    result: str

    @classmethod
    def start(cls, *args) -> str:
        try:
            cls.urls: str = args[0]
            cls.crawl_result: str = cls.crawl(cls)
            cls.prompt_template = args[1]
            cls.number_of_sentences = int(args[3])
            cls.tokenizer_name = args[2]
            cls.api_key = args[4]
            cls.tokenizer_class = get_tokenizer(cls.tokenizer_name)
            cls.summary = cls.non_gpt_summarize(cls, content=cls.crawl_result, contents=None)
            cls.prompt = get_prompt(cls.prompt_template, cls.summary)
            cls.result = cls.get_final_result(cls)
            return cls.result

        except KeyError:
            return "Error"

    def non_gpt_summarize(self, content: str | None, contents: List | None) -> str:
        textrank: TextRank = TextRank(self.tokenizer_class)
        if content:
            summarized: str = textrank.summarize(content, self.number_of_sentences)
        if contents:
            summarized: List = []
            for i, ctt in enumerate(contents):
                summarized.append(textrank.summarize(ctt, self.number_of_sentences))
            summarized = '\n'.join(summarized)
        return summarized

    def crawl(self) -> str:
        result = []
        for url in self.urls.split('\n'):
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            extracted_text = soup.get_text(strip=True)
            result.append(extracted_text)
        return "\n\n".join(result)

    def get_final_result(self):
        llm = OpenAI(model_name="gpt-4", openai_api_key=self.api_key)
        return llm.predict(self.prompt)