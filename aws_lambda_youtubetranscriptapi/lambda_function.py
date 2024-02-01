import os
import json
import urllib

from src.service import transcript_service, suffix_info_service


def lambda_handler(event, context):
    print(json.dumps(event))
    ytb_link = event.get('ytb_link')
    print(ytb_link)
    ytb_link = urllib.parse.unquote(ytb_link)
    print(ytb_link)
    ytb_link_and_suffix = suffix_info_service.parse(ytb_link)
    ytb_info = transcript_service.get_yt_info_by_link(ytb_link_and_suffix.ytb_link)
    ytb_info.update(ytb_link_and_suffix.__dict__)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": ytb_info
    }


if __name__ == '__main__':
    test_text = """"
  https://www.youtube.com/watch?v=bqkbHOvdKms
    d= 1. Introduction to the Course
    c= cut
    t= cut, intro
    """
    encode_test = urllib.parse.quote(test_text)
    print(lambda_handler({
        "ytb_link": encode_test
    }, None))
