import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from urllib.request import Request, urlopen

def download_comics(base_url, title, commic_url):
    ''' 
    =======================================
    DEMO:
    =======================================
    import download_comics
    base_url = 'D:/漫畫2'
    comics = {'街霸VS拳皇外傳': 'https://comic.acgn.cc/manhua-sfvskofwz.htm', 
              '街霸VS拳皇': 'https://comic.acgn.cc/manhua-sfvskof.htm'}
    for title, comic_url in comics.items():
        download_comics(base_url, title, comic_url)
    =======================================
    '''
    def get_chapter(file, url):
        # headers = {'User-Agent':'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        data = bs(response.text, 'html.parser')

        jpg_url_list = []
        for i in data.find_all(attrs={"style": "display:none;"}):
            jpg_url_list.append(i['_src'])
        # print(jpg_url_list)
        for j, url in enumerate(jpg_url_list[:]):
            print(j, url)
            if j+1 != int(url.split('/')[-1].split('.')[0]):
                print('檔名排序有問題 跳出!')
                exit()
            file_name = f'{base_url}/{title}/{file}/{str(j+1).rjust(3, "0")}.jpg'
            if os.path.isfile(file_name):
                print('檔案已存在，跳過~~')
                continue
            if any([i in url for i in ['索引超出了数组界限', 'indexoutofrangeexception']]):
                print(f'網站{file_name}此張圖broke，暫時略過並記錄在冊!!')
                if not os.path.isfile(f'{base_url}/{title}/http_error_520.txt'):
                    open(f'{base_url}/{title}/http_error_520.txt','a+')
                with open(f'{base_url}/{title}/http_error_520.txt','a+', encoding="utf-8") as f:
                    f.write(url + '\n' + file_name + '\n')
                    f.close()
                continue
            # print('mark_01')
            req = Request(url, headers=headers)
            # print('mark_02')
            try:
                # print('----------------')
                page = urlopen(req, timeout=15).read() # bytes
                # print(page)
                # print(type(page))
                # print('=========================')
            except Exception as e:
                if str(e) == 'HTTP Error 520: ':
                    print(f'網站{file_name}此張圖broke，暫時略過並記錄在冊!!')
                    if not os.path.isfile(f'{base_url}/{title}/http_error_520.txt'):
                        open(f'{base_url}/{title}/http_error_520.txt','a+')
                    with open(f'{base_url}/{title}/http_error_520.txt','a+', encoding="utf-8") as f:
                        f.write(url + '\n' + file_name + '\n')
                        f.close()
                    continue
                if 'timed out' in str(e):
                    print('超時錯誤 重新執行get_chapter(file, url)!!')
                    get_chapter(file, url)
                    continue
                    # exit()
                else:
                    print(333333333333333333)
                    print(str(e))
                    exit()
            f = open(file_name,'wb')
            f.write(page)
            f.close()

    # 先抓取看全部有幾集
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.get(commic_url, headers=headers)
    data = bs(response.text, 'html.parser')
    res = data.find(attrs={"id": "comic_chapter"})
    result = []
    for i in res.find_all('li'):
        chapter_num = i.text
        # tail_url = i.a.get("href")
        chapter_url = f'https://comic.acgn.cc/{i.a.get("href")}'
        # print(f'第{chapter}集，網址: {url}')
        result.append((chapter_num, chapter_url))

    # ConnectionResetError: [WinError 10054] 遠端主機已強制關閉一個現存的連線。

    # check集數正不正確
    abcd = []
    for i in result:
        print(i)
        abcd.append(int(i[1].split('view-')[1].replace('.htm', '')))
    # if len(abcd) == max(abcd) - min(abcd) + 1:print('check集數正確，往下執行中..........')
    # else:print('集數不正確，跳出!!');exit()


    # 每一章的下載url dataframe
    content = []
    for i in result:
        num = int(i[1].split('view-')[1].replace('.htm', ''))
        num = num - min(abcd) + 1
        content.append((num, i[0], i[1]))
        df = pd.DataFrame(content)
        df.rename(columns={0:'index', 1:'資料夾', 2:'連結'}, inplace=True)
        df = df.set_index('index').sort_values('index')
        print(df)

    # 建立根目錄
    if not os.path.isdir(f'{base_url}/{title}'):os.mkdir(f'{base_url}/{title}')

    # 讀已完成下載的資料夾有哪些
    if not os.path.isfile(f'{base_url}/{title}/download_tmp.txt'):
        open(f'{base_url}/{title}/download_tmp.txt','a+')
        finish_list = []
    else:
        with open(f'{base_url}/{title}/download_tmp.txt', 'r', encoding="utf-8") as f:
            finish_list = [line.split('\n')[0] for line in f.readlines()]
            print(finish_list)
            f.close()

    for i in range(len(df)):
        file = df.iloc[i]['資料夾']
        url = df.iloc[i]['連結']
        if file in finish_list:continue  # 已經下載的就略過
        print(f'檔案夾: {file} 連結: {url}')
        if not os.path.isdir(f'{base_url}/{title}/{file}'):os.mkdir(f'{base_url}/{title}/{file}')
        get_chapter(file, url)

        with open(f'{base_url}/{title}/download_tmp.txt', 'a', encoding="utf-8") as f:
            f.write(file + '\n')
            f.close()