"""
markitdown-hwp: MarkItDown plugin for HWP (한글 워드프로세서) files.
Internally uses docpler for parsing.
"""
from pathlib import Path
from typing import Any, BinaryIO


ACCEPTED_EXTENSIONS = frozenset({".hwp"})
ACCEPTED_MIME_TYPES = frozenset({
    "application/x-hwp",
    "application/haansofthwp",
    "application/vnd.hancom.hwp",
})


class HwpConverter:
    """MarkItDown converter for HWP files."""

    def accepts(
        self,
        file_stream: BinaryIO,
        stream_info: Any,
        **kwargs,
    ) -> bool:
        ext = getattr(stream_info, "extension", "") or ""
        mime = getattr(stream_info, "mimetype", "") or ""
        return ext.lower() in ACCEPTED_EXTENSIONS or mime in ACCEPTED_MIME_TYPES

    def convert(
        self,
        file_stream: BinaryIO,
        stream_info: Any,
        **kwargs,
    ):
        from markitdown import DocumentConverterResult
        from docpler.hwp import convert

        local_path = getattr(stream_info, "local_path", None)
        if not local_path:
            return None

        markdown_text = convert(local_path)
        return DocumentConverterResult(markdown=markdown_text)


class HwpConverterPlugin:
    """MarkItDown plugin entry point."""

    @staticmethod
    def register_converters(markitdown_instance, **kwargs):
        markitdown_instance.register_converter(HwpConverter())
