from urllib.parse import urlparse

FORBIDDEN_QUERY_ARGS = (
    'gclid',
    'yclid',
)


def cleanup_url(url: str) -> str:
    v = urlparse(url)
    params = [q.split('=') for q in v.query.split('&')]

    new_params = []
    for p in params:
        if p[0].startswith('utm_') or p[0] in FORBIDDEN_QUERY_ARGS:
            continue

        new_params.append(p)

    new_query = '&'.join(['='.join(p) for p in new_params])
    if new_query:
        new_query = '?' + new_query

    return v.scheme + '://' + v.hostname + v.path + new_query
