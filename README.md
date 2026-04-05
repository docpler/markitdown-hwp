# markitdown-hwp

[MarkItDown](https://github.com/microsoft/markitdown) plugin for HWP (한글 워드프로세서) files.
Powered by [docpler](https://pypi.org/project/docpler/).

## 설치

```bash
pip install markitdown-hwp
```

`markitdown`과 `docpler`가 자동으로 설치됩니다.

## 사용법

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True)
result = md.convert("document.hwp")
print(result.text_content)
```

별도 설정 없이 `enable_plugins=True`만 지정하면 HWP 파일이 자동으로 인식됩니다.

## 라이선스

MIT

## HWP 포맷 관련 고지

본 제품은 한글과컴퓨터의 한글 문서 파일(.hwp) 공개 문서를 참고하여 개발하였습니다.
