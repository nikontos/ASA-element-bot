# ASA-element-bot
ASA-element-bot

This is a script i made for my tribe so the element farm on Aberration gets automated.
The bot has a start point tp which is a room of dedis (we use those dedis to deposit element after a run is complete)
By using default R tp, it traverses to all the nodes which also have teleporters.

Opens inventory, crafts the element and moves on.
The bot has a reconnect functionality in case anything happens and doesnt access the node (earthquake or the inventory bug where you can't open it)
If a reconnect happens the bot tries to go back to his default position
After a set ammount of reconnects it skips the node
