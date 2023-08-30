"""
Tokenizer들을 작성해주세요.
모든 Tokenizer은 __call__ method가 작성되어있어야하며,
List[str]를 반환해야 합니다.

여기서 작성한 Tokenizer은 settings.py에 명시해주세요
"""

from konlpy.tag import Okt
from typing import List

class OktTokenizer:
    okt: Okt = Okt()
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens

    class Meta:
        name = 'Konlpy tokenizer'

class BaseTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens

    class Meta:
        name = 'Base tokenizer'