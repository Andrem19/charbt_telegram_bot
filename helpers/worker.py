import helpers.get_data as gd
import helpers.vizualization as viz


async def create_next_poll_pic():
    data_1, data_2 = await gd.chose_data()
    viz.save_candlesticks_pic(data_1, data_2)
