"""Parse a public GitHub pull request reference for the proof sandbox."""
import re
from urllib.parse import urlsplit

_PULL_PATH = re.compile(r"/([A-Za-z0-9-]+)/([A-Za-z0-9_.-]+)/pull/([1-9][0-9]*)/?")


def pull_request_parts(url: str) -> tuple[str, str, int]:
    """Return the owner, repository, and PR number from a canonical URL."""
    parts = urlsplit(url)
    match = _PULL_PATH.fullmatch(parts.path)
    if (parts.scheme != "https" or parts.netloc != "github.com"
            or parts.query or parts.fragment or match is None):
        raise ValueError("Use a canonical HTTPS GitHub pull request URL")
    owner, repository, number = match.groups()
    return owner, repository, int(number)
