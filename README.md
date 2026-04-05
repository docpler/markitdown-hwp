# markitdown-hwp

[MarkItDown](https://github.com/microsoft/markitdown) plugin for HWP documents.

HWP is a document format used by [Hancom Office](https://www.hancom.com/), the most widely used word processor in South Korea — commonly found in government, legal, and academic documents.

Powered by [docpler](https://pypi.org/project/docpler/).

## Installation

```bash
pip install markitdown-hwp
```

`markitdown` and `docpler` are installed automatically.

## Usage

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=True)
result = md.convert("document.hwp")
print(result.text_content)
```

No extra configuration needed — just `enable_plugins=True` and HWP files are recognized automatically.

---

# 한국어

HWP(한글 워드프로세서) 파일을 지원하는 [MarkItDown](https://github.com/microsoft/markitdown) 플러그인입니다.
내부적으로 [docpler](https://pypi.org/project/docpler/)를 사용합니다.

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

---

## License

[Business Source License 1.1 (BSL 1.1)](https://mariadb.com/bsl11/) — Free to use, cannot be provided as a managed service. Converts to Apache 2.0 on 2031-04-05.

## HWP Format Notice

This product was developed with reference to the HWP document file (.hwp) specification published by [Hancom](https://www.hancom.com/etc/hwpDownload.do).
