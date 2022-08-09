from youtube_statistics import YTstats


API_KEY = "AIzaSyAoJThWEhjo-kdY4tdz2-a_pR-fyNaEH1o"


# paste the channel id here
channel_id = "UC2qMi3uiorWxktkwoppgrKA"

yt = YTstats(API_KEY, channel_id)
yt.get_channel_statistics()
yt.dump()


