import pydest,bungoAPI,asyncio
destiny = pydest.Pydest(bungoAPI.APIKey)
categories = []
async def getUserStats(membershipID,membershipType):
    res2 = await destiny.api.get_historical_stats(membershipType,membershipID)
    print(res2)
    for item in res2["Response"]:
        categories.append(str(item))
        print(item)
   
    for subcat in res2["allPvP"]:
        print[subcat]







async def getUser():
    
    platform = input('Enter your platform (xbox[1], playstation[2], or pc[3]): ')
    username = input('Enter the username to locate: ')
    
    
    
    res = await destiny.api.search_destiny_player(platform, username)
    print(res)
    
    if res['ErrorCode'] == 1 and len(res['Response']) > 0:
        membershipID = res['Response'][0]['membershipId']
        membershipType = res['Response'][0]['membershipType']
        print(membershipID)
        print("---"*20)
        print("Player found!")
        print("Display Name: {}".format(res['Response'][0]['displayName']))
        print("Membership ID: {}".format(res['Response'][0]['membershipId']))
    else:
        print("Could not locate player.")
    
    await getUserStats(membershipID,membershipType)

    await destiny.close()



loop = asyncio.get_event_loop()
loop.run_until_complete(getUser())
loop.close()