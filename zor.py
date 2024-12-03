from TiktokApi import TiktokApi

def analyze_tiktok_trends(hashtag):
    try:
        with TiktokApi() as api:
            nazar = api.hashtag(name=hashtag).videos(count=10)
            print(f"{hashtag} ile alakalı en trend 10 video:\n")
            for idx, video in enumerate(nazar, start=1):
                print(f"Video {idx}:")
                print(f"  Creator: {video.author.username}")
                print(f"  Description: {video.desc}")
                print(f"  Likes: {video.stats.diggCount}")
                print(f"  Comments: {video.stats.commentCount}")
                print(f"  Shares: {video.stats.shareCount}")
                print(f"  Video URL: {video.video.playAddr}\n")
     except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    hashtag = input("Bir hashtag gir(# işareti olmadan): ")
    analyze_tiktok_trends(hashtag)   