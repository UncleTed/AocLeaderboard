import requests
import os
import bs4
from dotenv import load_dotenv

load_dotenv()

def make_cookie_jar():
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', os.getenv('SECRET'))
    return jar

def print_row(row):
    position = row.select_one('.privboard-position')
    score = position.next_sibling
    name = row.select_one('.privboard-name').getText()
    print(position.getText(), ' ',score, ' ', name)

def print_leader_board():
    leaders = 'https://adventofcode.com/2021/leaderboard/private/view/1031380'
    r = requests.get(leaders, cookies=make_cookie_jar())
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    people = soup.select('.privboard-row')
    people.pop(0)
    for p in people:
        print_row(p)


if __name__ == '__main__':
    print_leader_board()
