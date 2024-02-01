class SuffixInfo:
    def __init__(self):
        self.ytb_link: str = ""
        self.description: str = ""
        self.category: str = ""
        self.tags = list()


def parse(text: str) -> SuffixInfo:
    ans = SuffixInfo()
    text_array = text.split('\n')
    for row in text_array:
        row = row.strip()
        if row.startswith('http'):
            ans.ytb_link = row.strip()
        if row.startswith('d='):
            ans.description = row.replace('d=', '').strip()
        if row.startswith('c='):
            ans.category = row.replace('c=', '').strip()
        if row.startswith('t='):
            ans.tags = row.replace('t=', '').strip().split(',')
    return ans


if __name__ == '__main__':
    print(parse(""""
  https://www.youtube.com/watch?v=bqkbHOvdKms
    d= 1. Introduction to the Course
    c= cut
    t= cut, intro
    """).__dict__)
