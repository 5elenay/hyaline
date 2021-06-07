# Before Start
- Hyaline models is automatized so we don't added the most of the models like ban, member, role to this documentation. You should check [API Docs](https://discord.com/developers/docs/resources/) because everything in the API is also in these classes. That means we actually don't need to update this library if discord change objects.
- Hyaline events are also automatized too. So if discord adds a new event, you don't need to wait for new updates. Check all discord event list [here](https://discord.com/developers/docs/topics/gateway#commands-and-events-gateway-events). Event naming is full capitalized and no space. Example `Channel Update` is `CHANNEL_UPDATE` in hyaline.
- You can check hyaline helpers (`./helpers`) for better experience. 
    - **Example:** We all know we don't want to keep bitwise things in our mind and thats why we added intents & permissions helpers. Just import them and use it! 
    - **Another Example:** Discord API wants `Data URI` for images. Well, you can use image helper for both open and convert or just convert images!

- Hyaline has a built-in cache system. Currently supports: `Guild`, `Guild Member`, `Guild Channel` and `Message`. You don't need to fetch and fetch again. just use the cache (`<Session>.<ClientUser>.cache`)
- **Last thing:** hyaline currently **does not** support sharding. You can check `discord.py` for more user friendly library.

Now you can explore the functions! Also, you can contribute if you want to help us. Because, uh... why not?