import os
import json

from src.service import transcript_service


def lambda_handler(event, context):
    print(json.dumps(event))
    ytb_link = event.get('ytb_link')
    print(ytb_link)
    ytb_link = ytb_link.strip()
    ytb_info = transcript_service.get_yt_info_by_link(ytb_link)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": ytb_info
    }


if __name__ == '__main__':
    print(lambda_handler({
        "ytb_link": "  https://www.youtube.com/watch?v=bqkbHOvdKms"
    }, None))
