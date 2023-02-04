from steam import Steam
from website import settings

steam_key = settings.STEAM_API_KEY

steam = Steam("26977BDF1B922F2108E2C8319B056E1F")

# print(steam.users.search_user("l9_dmitry"))
# print(steam.users.get_user_details(steam_id="76561198839913782"))
# print(len(steam.users.get_user_friends_list("76561198839913782").get("friends")))
print(steam.apps.get_user_stats(steam_id=76561198839913782, app_id=570))
# print(steam.apps.search_games("dota 2"))