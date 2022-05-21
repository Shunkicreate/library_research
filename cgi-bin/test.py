#! /usr/bin/env python3
import sys
import io
import datetime as dt
current_time = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
print('Content-type: text/html')
print('')
print('<html lang=ja>')
print(' <head><meta http-equiv=\'Content-Type\' content=\'text/html; charset=utf-8\'/></head>')
print(' <body>')
print('    <h1>システムアーキテクトプログラミング演習</h1>')
print('    <div>現在時刻は{}</div>'.format(current_time))
print(' </body>')
print('</html>')