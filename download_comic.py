from comic import download_comics

base_url = 'D:/漫畫'
comics = {
        # '街霸VS拳皇外傳': 'https://comic.acgn.cc/manhua-sfvskofwz.htm',
        # '街霸VS拳皇': 'https://comic.acgn.cc/manhua-sfvskof.htm',
        # '范馬刃牙': 'https://comic.acgn.cc/manhua-fmry.htm',
        # '街霸4': 'https://comic.acgn.cc/manhua-jtbw4.htm',
        # '神兵玄奇Ⅰ': 'https://comic.acgn.cc/manhua-shenbingxuanqi.htm',
        # '射鵰英雄傳': 'https://comic.acgn.cc/manhua-shediaoyingxiongzhuan.htm',
        # '神鵰俠侶': 'https://comic.acgn.cc/manhua-sdxl.htm',
        # '神劍闖江湖': 'https://comic.acgn.cc/manhua-lkjx.htm',
        # 'I』』S': 'https://comic.acgn.cc/manhua-is.htm',
        # '灌藍高手': 'https://comic.acgn.cc/manhua-lanqiufeirenquancai.htm',
        # '幽游白書': 'https://comic.acgn.cc/manhua-yybsyuyuhakusho.htm',

        # '天子傳奇1': 'https://comic.acgn.cc/manhua-tianzi1.htm',
        # '天子傳奇2': 'https://comic.acgn.cc/manhua-tianzi2.htm',
        # '天子傳奇3': 'https://comic.acgn.cc/manhua-tianzi3.htm',
        # '天子傳奇4': 'https://comic.acgn.cc/manhua-tianzi4.htm',
        # '天子傳奇5': 'https://comic.acgn.cc/manhua-tianzi5.htm',
        # '天子傳奇6': 'https://comic.acgn.cc/manhua-tianzil6.htm',
        # '天子傳奇7': 'https://comic.acgn.cc/manhua-tianzichuanqi7.htm',
        # '天子傳奇8': 'https://comic.acgn.cc/manhua-tzcq8.htm',

        '蜀山劍俠傳':'https://comic.acgn.cc/manhua-shushanjianxiazhuan.htm'
        # '雪山飛狐':'https://comic.acgn.cc/manhua-xsfh.htm'
        # '倚天屠龍記':'https://comic.acgn.cc/manhua-yttlj.htm'
        # '神兵前傳3':'https://comic.acgn.cc/manhua-shenbingchuanqi3.htm'
        # '神兵玄奇外傳':'https://comic.acgn.cc/manhua-sbxqwz.htm'
        # '拳皇99':'https://comic.acgn.cc/manhua-kof99.htm'
        # '風雲2電影漫畫版':'https://comic.acgn.cc/manhua-fy2dymhb.htm'
        # '天殛':'https://comic.acgn.cc/manhua-tianji.htm'
        # '新著如來神掌':'https://comic.acgn.cc/manhua-xinzhurulaishenzhang.htm'
        # '七種武器':'https://comic.acgn.cc/manhua-qzwq.htm'
        # '英雄無淚':'https://comic.acgn.cc/manhua-yxwl.htm'
        # '風雲':'https://comic.acgn.cc/manhua-fengyun.htm'

        # '聖鬥士星矢': 'https://comic.acgn.cc/manhua-shengdoushi.htm',
        # '聖鬥士-冥王神話': 'https://comic.acgn.cc/manhua-shengdoushi-mingwangshenhua.htm',
        # '七龍珠完全版': 'https://comic.acgn.cc/manhua-qilongzhuwanquanban.htm',
        # '七龍珠 超次元亂戰': 'https://comic.acgn.cc/manhua-chaociyuanluanzhan.htm',
        # '春秋戰雄': 'https://comic.acgn.cc/manhua-chunqiuzhanxiong.htm',
          }
for title, comic_url in comics.items():
    download_comics(base_url, title, comic_url)

# HTTP Error 409: Conflict