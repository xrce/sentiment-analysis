from prettytable import PrettyTable
from ntscraper import Nitter
import csv

buzzer = ["PakPrabowo", "DadiPresidenku", "PrabowoGibran", "GaweAyem",
          "BersamaIndonesiaMaju", "PrabowoGemoy", "KodeKita08Gemoy", "2024gantiwarna"
          "IndonesiaSentris", "02Melanjutkan", "AnakMudaIndonesiaEmas", "MenangSeputaran"]
official = ["@liputan6dotcom", "@tempodotco", "@Metro_TV", "@kompascom",
            "@KompasTV", "@hariankompas", "@TirtoID", "@pikiran_rakyat",
            "@CNNIndonesia", "@KATADATAcoid", "@jpnncom", "@Beritasatu",
            "@GATRA_com", "@antaranews", "@mediasemut", "@DppAliansi",
            "@RepelitaO", "@kabaridcom", "@IDNTimes", "@kumparan",
            "@voidotid", "@okezonenews", "@OposisiCerdas", "@OfficialDPP_PBB",
            "@cnbcindonesia", "@VIVAcoid", "@democrazymedia", "@KompasData"]

nbuzzer, invalid, irrelevant, duplicate = 0, 0, 0, 0

keyword = "prabowo gibran"
jumlah = 1000
start = "2023-12-25"
end = "2023-12-26"
output = "tweet.csv"

if __name__ == "__main__":
    scraper = Nitter(log_level=1, skip_initial_check=True)
    results = scraper.get_tweets(keyword, mode="term", number=jumlah, since=start, until=end)
    tweets = results['tweets']

    table = PrettyTable()
    table.field_names = ["Date", "Username", "Text", "Comments", "Likes"]

    for tweet in tweets:
        link = tweet['link']
        text = tweet['text']
        user = tweet['user']
        name = user['name']
        username = user['username']
        profile = user['profile_id']
        avatar = user['avatar']
        date = tweet['date']
        retweet = tweet['is-retweet']
        stats = tweet['stats']
        comments = stats['comments']
        retweets = stats['retweets']
        quotes = stats['quotes']
        likes = stats['likes']
        
        if any(teks in text for teks in buzzer): nbuzzer += 1
        elif any(name in username for name in official): irrelevant += 1
        elif any(text in row[2] for row in table._rows): duplicate += 1
        elif text == "" or not text: invalid += 1
        else: table.add_row([date, username, text])

    table.align["Text"] = "l"
    table.max_width["Text"] = 100
    
    with open(output, "w", newline="", encoding="utf-8") as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(table.field_names)
        csv_writer.writerows(table._rows)
    
    print(table)
    print(f"\n\n [*] Berhasil menghapus {invalid} tweet kosong")
    print(f" [*] Berhasil menghapus {nbuzzer} tweet yang terdeteksi sebagai buzzer")
    print(f" [*] Berhasil menghapus {irrelevant} tweet yang terdeteksi akun non-relevan")
    print(f" [*] Berhasil menghapus {duplicate} tweet yang terdeteksi sebagai duplikat")
    print(f" [*] Data {len(table._rows)} tweet disimpan di {output}")