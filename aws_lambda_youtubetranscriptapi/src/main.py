import urllib
from urllib import parse


def split_text(text: str, split_symbol: str = '\n') -> list:
    return text.split(split_symbol)


def lambda_handler(event, context):
    function = event.get('function')
    text = event.get('text')
    print(text)
    text = parse.unquote(text)
    ans = None
    if function == 'split_text':
        ans = split_text(text)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "function": function,
        "body": ans
    }


if __name__ == '__main__':
    encode_test = parse.quote("""
        a
        b
        c
    """)
    resp = lambda_handler({
        "function": "split_text",
        "text": encode_test
    }, None)
    print(resp)
