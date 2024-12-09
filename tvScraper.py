#!/usr/bin/python3

import argparse, requests, time, sys
from bs4 import BeautifulSoup

def parse_args():    
    parser = argparse.ArgumentParser(description='Print the TV scheduling for given day', prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=40))
    parser.add_argument('day', help='Choose the day to check for TV schedule')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--movies', help='print only TV movies channels', action='store_true')
    group.add_argument('-s', '--sports', help='print only TV sports channels', action='store_true')
    parser.add_argument('-c', '--channel', help='choose a specific channel')
    return parser.parse_args()

def main():
    args = parse_args()
    if args.day not in ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'):
        print("Invalid day! Only the following days are accepted: segunda, terca, quarta, quinta, sexta, sabado, domingo. (Type them precisely like that)")
        sys.exit()
    if args.channel:
        channels = [args.channel]
    elif args.movies:
        channels = ['nos-studios', 'hollywood', 'axn', 'axn-black', 'axn-white', 'fox', 'fox-life', 'fox-movies', 'cinemundo', 'syfy', 'amc', 'tvc1', 'tvc2', 'tvc3', 'tvc4', 'fox-comedy']
    elif args.sports:
        channels = ['sport-tv-mais', 'sport-tv1', 'sport-tv2', 'sport-tv3', 'sport-tv4', 'sport-tv5', 'eleven-sports-1', 'eleven-sports-2', 'eleven-sports-3']
    else:
        channels = ['sport-tv-mais', 'sport-tv1', 'sport-tv2', 'sport-tv3', 'sport-tv4', 'sport-tv5', 'eleven-sports-1', 'eleven-sports-2', 'eleven-sports-3', 'nos-studios', 'hollywood', 'axn', 'axn-black', 'axn-white', 'fox', 'fox-life', 'fox-movies', 'cinemundo', 'syfy', 'amc', 'tvc1', 'tvc2', 'tvc3', 'tvc4', 'fox-comedy']
    
    for channel in channels:
        request = requests.get('https://tudonumclick.com/programacao-tv/{}/{}/'.format(channel, args.day)).text
        soup = BeautifulSoup(request, 'lxml')
    
        hour = []
        program = []
        resume = []

        for match in soup.find_all('p', class_='article-info ml10 fs14 left'):
            hour.append(match.text)

        for match in soup.find_all('b', class_='ml10 dib'):
            program.append(match.text)
        
        for match in soup.find_all('p', class_='fs16 p10 channel_desc hidden'):
            resume.append(match.text)

        print('\n##', channel.upper(), '##\n')
        
        try:
            for i in range(2):
                print(hour[i], '-', program[i], '| Resumo:', resume[i])
        except IndexError:
            pass

        time.sleep(1)

if __name__ == '__main__':
    main()
