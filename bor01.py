"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from  bot03 import *
from  bo02 import *
from config import API_TOKEN
#config faylda faqat token saqanadi
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db_create()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    telegram_id = message.from_user.id
    username = message.from_user.username

####################################### telfon raqam va til##################
#################################################
#########################################################################




    data = db_select(telegram_id)
    print(data)
    if data is None:
        db_insert(telegram_id,username)
        await message.reply_photo(
        photo=open('images/evos.jpg','rb'),
caption="""Assalomu alaykum\n tilni tanlamng""",reply_markup=til,)
        

    else:
        await message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""salom""",reply_markup=menu,)
        


############################pastki menu #######################################



@dp.callback_query_handler(text="uz")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""Assalomu alaykum\n siz uzbek tilini tanladingiz\n telfon raqamingizni kiriting""",reply_markup=contact,)




###########################rus tili javobi #########################################



@dp.callback_query_handler(text="ru")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/til.jpg','rb'),
caption="""Assalomu alaykum\n siz rus tilini tanladingiz\nhozir sozlanmoqda!!!""")


#########################ingiliz tili javobi #############################

@dp.callback_query_handler(text="eng")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/til.jpg','rb'),
caption="""Assalomu alaykum\n siz rus tilini tanladingiz\nhozir sozlanmoqda!!!""")

############################## == == ############################################


@dp.message_handler(content_types=['contact'])
async def echo(message: types.Message):
    phone_number = message.contact['phone_number']
    db_update(message.from_user.id,phone_number)
    print(phone_number)
    await message.answer_photo(
        photo=open('images/til.jpg','rb'),
caption="""qabul qilindi""",reply_markup=location)

# @dp.message_handler(content_types=['contact'])
# async def echo(message: types.Message):
#     phone_number = message.contact['phone_number']
#     db_update(message.from_user.id,phone_number)
#     print(phone_number)
#     await message.answer('qabul qilindi',reply_markup=location)
############################## == == ############################################

@dp.message_handler(content_types=['location'])
async def echo(message: types.Message):
    lat_x = message.location['latitude']
    lon_y = message.location['longitude']
    db_update_location(message.from_user.id,lat_x,lon_y)
    # location = message.location['location']
    print(lat_x,lon_y)

# @dp.message_handler(content_types=['location'])
# async def echo(message: types.Message):
#     lat_x = message.location['latitude']
#     lon_y = message.location['longitude']
#     db_update_location(message.from_user.id,lon_y,lon_y)
#     print(lat_x,lon_y)

    await message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""joylashuvingiz qabul qilindi""",reply_markup=menu,)











########################## aloqa javobi ######################################
@dp.message_handler(text="☎️ Aloqa")
async def knopka(message: types.Message):
    await message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""sozlanmoqda!!!""")


################################# sozlamalar javobi#########################################

@dp.message_handler(text="⚙️ Sozlamalar")
async def knopka(message: types.Message):
    await message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""sozlanmoqda!!!""")


########################################################################################
##############################  bosh menu ################################################
####################################################################################

@dp.message_handler(text="🍽 maxsulotlar")
async def knopka(message: types.Message):
    await message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""tanlang!!!""",reply_markup=bosh_menu)



######################################################################


@dp.callback_query_handler(text="orqaga01")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""✅Marxamat  menu!!!""",reply_markup=bosh_menu)


######################################################################


@dp.callback_query_handler(text="orqaga_bosh")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""✅Marxamat  menu!!!""",reply_markup=bosh_menu)

######################################################################


# @dp.callback_query_handler(text="orqaga_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer('✅Marxamat ichimliklar  menusi!!!',reply_markup=ichimlik_menu)

#################### == == ###################################




@dp.callback_query_handler(text="orqaga_lavash")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat lavashlar menusi!!!',reply_markup=lavash_menu)


#################### ==orqaga choy == ###################################




# @dp.callback_query_handler(text="orqaga_choy_00")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer('✅Marxamat ichim menusi!!!',reply_markup=raqamlar_choy)


#################### ==orqaga choy raqamdan== ###################################







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################














######################################################################

    
@dp.callback_query_handler(text="lavash")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashlar.jpg','rb'),
caption="""✅Marxamat lavashlar menusi!!!""",reply_markup=lavash_menu)



######################################################################

    
@dp.callback_query_handler(text="orqaga_lavash_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavashlar.jpg','rb'),
caption="""✅Marxamat lavashlar menusi!!!""",reply_markup=lavash_menu)


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



#################################### lavashning ichiki menyusi #####################################################




@dp.callback_query_handler(text="lavash_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Kategoriyalardan birini tanlang!!!',reply_markup=lavash_menu_mol)



@dp.callback_query_handler(text="orqaga_lavash_raqamdan_mol_cm")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅Mol go'shtli classik lavash narxi 28 000, mini lavash narxi 24 000 so'm",reply_markup=lavash_menu_mol)


########################################  === katigoriya  classik === #########################################################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_lavash.jpg','rb'),
caption="""✅Mol go'shtli classik lavash narxi 28 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_mol_classik)


##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {1*28000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {2*28000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {3*28000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {4*28000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {5*28000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {6*28000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {7*28000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {8*28000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {9*28000} so'm\n ✅lavashlar soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)




##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli classik lavash narxi {10*28000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_mol_classik)





##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_mol_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_lavash.jpg','rb'),
caption="""✅Mol go'shtli classik lavash narxi 28 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_mol_classik)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_lavash.jpg','rb'),
caption="""✅Mol go'shtli mini lavash narxi 24 000 so'm\n ✅Marxamat lavash sonini tanlang👍""" ,reply_markup=raqamlar_lavash_mol_mini)


##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {1*24000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)



##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {2*24000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {3*24000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {4*24000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {5*24000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {6*24000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {7*24000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {8*24000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {9*24000} so'm\n ✅lavashlar soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)




##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli mini lavash narxi {10*24000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_mol_mini)







##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_mol_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/mol_lavash.jpg','rb'),
caption="""✅Mol go'shtli mini lavash narxi 24 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_mol_mini)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


#####################################== == orqaga== ==   ########################################################
##############################################################



@dp.callback_query_handler(text="lavash_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_lavash.jpg','rb'),
caption="""Narxi: classik 25 000, mini 21 000 so'm\n Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez\n✅Kategoriyalardan birini tanlang!!!""",reply_markup=lavash_menu_tovuq)


#####################################== == orqaga== ==   ########################################################
##############################################################



@dp.callback_query_handler(text="orqaga_lavash_raqamdan_toviq_dm")
async def knopka(call: types.CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/tovuq_lavash.jpg','rb'),
caption="""Narxi: classik 25 000 so'm\n Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez\n✅Kategoriyalardan birini tanlang!!!""",reply_markup=lavash_menu_tovuq)





##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅tovuq go'shtli classik lavash narxi 25 000 so'm\n ✅Marxamat lavash sonini tanlang👍 ",reply_markup=raqamlar_lavash_tovuq_classik)






##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {1*25000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)




##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {2*25000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {3*25000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {4*25000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {5*25000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################          6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {6*25000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {7*25000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {8*25000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {9*25000} so'm\n ✅lavashlar soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)





##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli classik lavash narxi {10*25000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_classik)




##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_tovuq_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_lavash.jpg','rb'),
caption="""Narxi: classik 25 000 so'm\n Tarkibi:Xamir,go'sht,chips,pomidor,bodring,sous,moyonez\n✅Kategoriyalardan birini tanlang!!!""",reply_markup=lavash_menu_tovuq)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_lavash.jpg','rb'),
caption="""✅tovuq go'shtli mini lavash narxi 21 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_tovuq_mini)






##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {1*21000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)




##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {2*21000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {3*21000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {4*21000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {5*21000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################       6      #################################################




@dp.callback_query_handler(text="oltinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {6*21000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {7*21000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {8*21000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {9*21000} so'm\n ✅lavashlar soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli mini lavash narxi {10*21000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_mini)





##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_tovuq_mini")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/tovuq_lavash.jpg','rb'),
caption="""✅tovuq go'shtli mini lavash narxi 21 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_tovuq_mini)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash02.jpg','rb'),
caption="""✅Mol go'shtli qalanpirli lavash narxi 25 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_mol_q)






##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {1*25000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)



##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {2*25000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################     3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {3*25000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {4*25000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {5*25000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {6*25000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {7*25000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {8*25000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {9*25000} so'm\n ✅lavashlar soni 9  ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅Mol go'shtli qalanpirli lavash narxi {10*25000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_mol_q)




##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash02.jpg','rb'),
caption="""✅Mol go'shtli qalanpirli lavash narxi 25 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_mol_q)











##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash02.jpg','rb'),
caption="""✅tovuq go'shtli qalanpirli lavash narxi 23 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_tovuq_q)






##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {1*23000} so'm\n ✅lavashlar soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)




##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {2*23000} so'm\n ✅lavashlar soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {3*23000} so'm\n ✅lavashlar soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      4       #################################################




@dp.callback_query_handler(text="tortinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {4*23000} so'm\n ✅lavashlar soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {5*23000} so'm\n ✅lavashlar soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {6*23000} so'm\n ✅lavashlar soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {7*23000} so'm\n ✅lavashlar soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {8*23000} so'm\n ✅lavashlar soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {9*23000} so'm\n ✅lavashlar soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)





##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅tovuq go'shtli qalanpirli lavash narxi {10*23000} so'm\n ✅lavashlar soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_tovuq_q)






##########################  +++  ++++ ##################################################






@dp.callback_query_handler(text="orqaga_lavash_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/lavash02.jpg','rb'),
caption="""✅tovuq go'shtli qalanpirli lavash narxi 23 000 so'm\n ✅Marxamat lavash sonini tanlang👍 """,reply_markup=raqamlar_lavash_tovuq_q)










##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




########################### ===  lavash tovuq ==== ################################









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





@dp.callback_query_handler(text="fitter")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fittr.jpg','rb'),
caption="""✅fitter narxi 20 000 so'm\n ✅Marxamat fitter sonini tanlang👍""",reply_markup=raqamlar_lavash_fittr)






##########################  +++  ++++ ##################################################
##########################      1       #################################################




@dp.callback_query_handler(text="birinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {1*20000} so'm\n ✅fitter soni 1 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)





##########################  +++  ++++ ##################################################
##########################      2       #################################################




@dp.callback_query_handler(text="ikkinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {2*20000} so'm\n ✅fitter soni 2 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      3       #################################################




@dp.callback_query_handler(text="uchunchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {3*20000} so'm\n ✅fitter soni 3 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      4       #################################################



@dp.callback_query_handler(text="tortinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {4*20000} so'm\n ✅fitter soni 4 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      5       #################################################




@dp.callback_query_handler(text="beshinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {5*20000} so'm\n ✅fitter soni 5 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      6       #################################################




@dp.callback_query_handler(text="oltinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {6*20000} so'm\n ✅fitter soni 6 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      7       #################################################




@dp.callback_query_handler(text="yettinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {7*20000} so'm\n ✅fitter soni 7 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      8       #################################################




@dp.callback_query_handler(text="sakiznchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {8*20000} so'm\n ✅fitter soni 8 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      9       #################################################




@dp.callback_query_handler(text="toqqizinchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {9*20000} so'm\n ✅fitter soni 9 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)

##########################  +++  ++++ ##################################################
##########################      10       #################################################




@dp.callback_query_handler(text="oninchi_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅fitter narxi {10*20000} so'm\n ✅fitter soni 10 ta👍 ",reply_markup=contact_oxiri_lavash_fittr)




##########################  +++  ++++ ##################################################





@dp.callback_query_handler(text="orqaga_lavash_fittr")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fittr.jpg','rb'),
caption="""✅fitter narxi 20 000 so'm\n ✅Marxamat fitter sonini tanlang👍""",reply_markup=raqamlar_lavash_fittr)




####################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






###########E#3333332222222222222 ==  BOSH MENULAR === 2222222222222222222222222222222#################################


########################### ===  HOD DOG BOSH ==== ################################




@dp.callback_query_handler(text="hoddog")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_dalb.jpg','rb'),
caption="""✅Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅Marxamat Hod Dog menusi!!!""",reply_markup=hoddog_menu)





@dp.callback_query_handler(text="orqaga_hoddog_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_dalb.jpg','rb'),
caption="""✅Tarkibi:✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅Marxamat Hod Dog menusi!!!""",reply_markup=hoddog_menu)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="baget_hoddog")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_dalb.jpg','rb'),
caption="""✅✅Baget Dabl hoddog narxi 18 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_baget)







####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="birinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {1*18000} so'm\n✅✅maxsulot soni 1 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)

#############







####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="ikkinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {2*18000} so'm\n✅✅maxsulot soni 2 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="uchunchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {3*18000} so'm\n✅✅maxsulot soni 3 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="tortinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {4*18000} so'm\n✅✅maxsulot soni 4 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="beshinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {5*18000} so'm\n✅✅maxsulot soni 5 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="oltinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {6*18000} so'm\n✅✅maxsulot soni 6 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="yettinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {7*18000} so'm\n✅✅maxsulot soni 7 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="sakiznchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {8*18000} so'm\n✅✅maxsulot soni 8 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="toqqizinchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {9*18000} so'm\n✅✅maxsulot soni 9 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)






####################     == hoddog menuchasi == #########################




@dp.callback_query_handler(text="oninchi_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Baget Dabl hoddog narxi {10*18000} so'm\n✅✅maxsulot soni 10 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_baget)


####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_hoddog_baget")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_dalb.jpg','rb'),
caption="""✅✅Baget Dabl hoddog narxi 18 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_baget)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="classik_hoddog")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog.jpg','rb'),
caption="""✅✅classik hoddog narxi 12 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_classik)







####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="birinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {1*12000} so'm\n✅✅maxsulot soni 1 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {2*12000} so'm\n✅✅maxsulot soni 2 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {3*12000} so'm\n✅✅maxsulot soni 3 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {4*12000} so'm\n✅✅maxsulot soni 4 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {5*12000} so'm\n✅✅maxsulot soni 5 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {6*12000} so'm\n✅✅maxsulot soni 6 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {7*12000} so'm\n✅✅maxsulot soni 7 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {8*12000} so'm\n✅✅maxsulot soni 8 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {9*12000} so'm\n✅✅maxsulot soni 9 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)





####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oninchi_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅classik hoddog narxi {10*12000} so'm\n✅✅maxsulot soni 10 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_classik)



####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_hoddog_classik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog.jpg','rb'),
caption="""✅✅classik hoddog narxi 12 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_classik)










##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="tovuqli_hoddog")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog.jpg','rb'),
caption="""✅✅tovuqli hoddog narxi 10 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="birinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {1*10000} so'm\n✅✅maxsulot soni 1 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {2*10000} so'm\n✅✅maxsulot soni 2 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {3*10000} so'm\n✅✅maxsulot soni 3 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {4*10000} so'm\n✅✅maxsulot soni 4 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {5*10000} so'm\n✅✅maxsulot soni 5 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {6*10000} so'm\n✅✅maxsulot soni 6 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {7*10000} so'm\n✅✅maxsulot soni 7 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {8*10000} so'm\n✅✅maxsulot soni 8 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {9*10000} so'm\n✅✅maxsulot soni 9 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oninchi_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅tovuqli hoddog narxi {10*10000} so'm\n✅✅maxsulot soni 10 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_tovuqli)


####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_hoddog_tovuqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog.jpg','rb'),
caption="""✅✅tovuqli hoddog narxi 10 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_tovuqli)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="kar_hoddog")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_k.jpg','rb'),
caption="""✅✅Korolevsiky hoddog narxi 20 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_kar)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="birinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {1*20000} so'm\n✅✅maxsulot soni 1 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {2*20000} so'm\n✅✅maxsulot soni 2 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {3*20000} so'm\n✅✅maxsulot soni 3 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {4*20000} so'm\n✅✅maxsulot soni 4 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {5*20000} so'm\n✅✅maxsulot soni 5 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {6*20000} so'm\n✅✅maxsulot soni 6 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {7*20000} so'm\n✅✅maxsulot soni 7 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {8*20000} so'm\n✅✅maxsulot soni 8 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {9*20000} so'm\n✅✅maxsulot soni 9 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)




####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oninchi_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Korolevsiky hoddog narxi {10*20000} so'm\n✅✅maxsulot soni 10 ta\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.",reply_markup=contact_oxiri_hoddog_kar)





####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_hoddog_kar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/hoddog_k.jpg','rb'),
caption="""✅✅Korolevsiky hoddog narxi 20 000 so'm\nTarkibi:✅✅Kulcha,sosiska2x,ketchup va xantal,qovurilgan piyoz.\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_hoddog_kar)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



########################### ===  SENDVICH BOSH ==== ################################



@dp.callback_query_handler(text="sendvich")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅Marxamat Sendvich menusi!!!""",reply_markup=sendvich_menu)

########################### ===  SENDVICH BOSH ==== ################################



@dp.callback_query_handler(text="orqaga_sendvich_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅Marxamat Sendvich menusi!!!""",reply_markup=sendvich_menu)

##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="classik_sendvich")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅✅Sendvich classik  narxi 27 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="birinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich classik narxi {1*27000} so'm\n✅✅maxsulot soni 1 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {2*27000} so'm\n✅✅maxsulot soni 2 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich classik  narxi {3*27000} so'm\n✅✅maxsulot soni 3 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {4*27000} so'm\n✅✅maxsulot soni 4 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {5*27000} so'm\n✅✅maxsulot soni 5 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich classik  narxi {6*27000} so'm\n✅✅maxsulot soni 6 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {7*27000} so'm\n✅✅maxsulot soni 7 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {8*27000} so'm\n✅✅maxsulot soni 8 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {9*27000} so'm\n✅✅maxsulot soni 9 ta.",reply_markup=contact_oxiri_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oninchi_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich  classik narxi {10*27000} so'm\n✅✅maxsulot soni 10 ta.",reply_markup=contact_oxiri_sendvich_c)


####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_sendvich_c")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅✅Sendvich  classik narxi 27 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_sendvich_c)



####################     ==


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="tovuqli_sendvich")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅✅Sendvich narxi 23 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_sendvich_c)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="birinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {1*23000} so'm\n✅✅maxsulot soni 1 ta.",reply_markup=contact_oxiri_sendvich_ct)


####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {2*23000} so'm\n✅✅maxsulot soni 2 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {3*23000} so'm\n✅✅maxsulot soni 3 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {4*23000} so'm\n✅✅maxsulot soni 4 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {5*23000} so'm\n✅✅maxsulot soni 5 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {6*23000} so'm\n✅✅maxsulot soni 6 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {7*23000} so'm\n✅✅maxsulot soni 7 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {8*23000} so'm\n✅✅maxsulot soni 8 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {9*23000} so'm\n✅✅maxsulot soni 9 ta.",reply_markup=contact_oxiri_sendvich_ct)



####################     == hoddog menuchasi == #########################

@dp.callback_query_handler(text="oninchi_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Sendvich tovuqli narxi {10*23000} so'm\n✅✅maxsulot soni 10 ta.",reply_markup=contact_oxiri_sendvich_ct)


####################     == hoddog menuchasi == #########################



@dp.callback_query_handler(text="orqaga_sendvich_ct")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sendvish.jpg','rb'),
caption="""✅✅Sendvich tovuqli narxi 23 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_sendvich_ct)



####################     ==


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



########################### ===  BURGER BOSH ==== ################################



@dp.callback_query_handler(text="burger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅Marxamat Burger menusi!!!""",reply_markup=burger_menu)



########################### ===  BURGER BOSH ==== ################################



@dp.callback_query_handler(text="orqaga_burger_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅Marxamat Burger menusi!!!""",reply_markup=burger_menu)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




@dp.callback_query_handler(text="gamburger")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅✅gamburger narxi 25 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gamburger)



####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {1*25000} so'm\n✅✅maxsulot soni 1 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {2*25000} so'm\n✅✅maxsulot soni 2 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {3*25000} so'm\n✅✅maxsulot soni 3 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {4*25000} so'm\n✅✅maxsulot soni 4 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {5*25000} so'm\n✅✅maxsulot soni 5 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {6*25000} so'm\n✅✅maxsulot soni 6 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {7*25000} so'm\n✅✅maxsulot soni 7 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {8*25000} so'm\n✅✅maxsulot soni 8 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {9*25000} so'm\n✅✅maxsulot soni 9 ta.",reply_markup=contact_oxiri_gamburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="oninchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅gamburger narxi {10*25000} so'm\n✅✅maxsulot soni 10 ta.",reply_markup=contact_oxiri_gamburger)


####################     == burger menuchasi == #########################
##########################  +++  ++++ ##################################################




@dp.callback_query_handler(text="orqaga_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅✅gamburger narxi 25 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gamburger)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




@dp.callback_query_handler(text="chizburger")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅✅chizburger narxi 29 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_chizburger)



####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {1*29000} so'm\n✅✅maxsulot soni 1 ta.",reply_markup=contact_oxiri_chizburger)



####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {2*29000} so'm\n✅✅maxsulot soni 2 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {3*29000} so'm\n✅✅maxsulot soni 3 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {4*29000} so'm\n✅✅maxsulot soni 4 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {5*29000} so'm\n✅✅maxsulot soni 5 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {6*29000} so'm\n✅✅maxsulot soni 6 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {7*29000} so'm\n✅✅maxsulot soni 7 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {8*29000} so'm\n✅✅maxsulot soni 8 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {9*29000} so'm\n✅✅maxsulot soni 9 ta.",reply_markup=contact_oxiri_chizburger)


####################     ==burger menuchasi == #########################

@dp.callback_query_handler(text="birinchi_gamburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅chizburger narxi {10*29000} so'm\n✅✅maxsulot soni 10 ta.",reply_markup=contact_oxiri_chizburger)

#########################  +++  ++++ ##################################################




@dp.callback_query_handler(text="orqaga_chizburger")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/burger.jpg','rb'),
caption="""✅✅chizburger narxi 29 000 so'm\n✅✅marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_chizburger)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






########################### ===  shaurma bosh ==== ################################



@dp.callback_query_handler(text="shaurma")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/shaurma.jpg','rb'),
caption="""✅Marxamat Shaurma menusi!!!""",reply_markup=shaurma_menu)





########################### ===  shaurma bosh ==== ################################



@dp.callback_query_handler(text="orqaga_shaurma_raqamdan")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/shaurma.jpg','rb'),
caption="""✅Marxamat Shaurma menusi!!!""",reply_markup=shaurma_menu)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="shaurma_mol")
async def knopka(call: types.CallbackQuery):
     await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Mol go'shtli shaurma\n✅✅Narxi 26 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_mol)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {1*26000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_shaurma_mol)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {2*26000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {3*26000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {4*26000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {5*26000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {6*26000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {7*26000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {8*26000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {9*26000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli shaurma\n✅✅Narxi {10*26000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_shaurma_mol)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_shaurma_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Mol go'shtli shaurma\n✅✅Narxi 26 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_mol)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Tovuq go'shtli shaurma\n✅✅Narxi 23 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_tovuq)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {1*23000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {2*23000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {3*23000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {4*23000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {5*23000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {6*23000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_shaurma_tovuq)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {7*23000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {8*23000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_shaurma_tovuq)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {9*23000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_shaurma_tovuq)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli shaurma\n✅✅Narxi {10*23000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_shaurma_tovuq)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_shaurma_tovuq")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Tovuq go'shtli shaurma\n✅✅Narxi 23 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_tovuq)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi 26 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_mol_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {1*26000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_shaurma_mol_q)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtl, Qalanpirlii shaurma\n✅✅Narxi {2*26000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {3*26000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {4*26000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {5*26000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {6*26000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {7*26000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {8*26000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {9*26000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi {10*26000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_shaurma_mol_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_shaurma_mol_q")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Mol go'shtli, Qalanpirli shaurma\n✅✅Narxi 26 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_mol_q)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi 23 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_tovuq_q)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {1*23000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {2*23000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {3*23000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {4*23000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {5*23000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {6*23000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)

####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {7*23000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {8*23000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {9*23000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi {10*23000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_shaurma_tovuq_q)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_shaurma_tovuq_q")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/shaurma2.jpg','rb'),
caption="""✅✅Tovuq go'shtli, Qalanpirli shaurma\n✅✅Narxi 23 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_shaurma_tovuq_q)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




@dp.callback_query_handler(text="gazak")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat Gazak menusi!!!',reply_markup=gazak_menu)

##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


@dp.callback_query_handler(text="orqaga_gazak_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat Gazak menusi!!!',reply_markup=gazak_menu)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/fireee.jpg','rb'),
caption="""✅✅15 fri👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {1*11000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_gazak_15_firi)


####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {2*11000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {3*11000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {4*11000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {5*11000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {6*11000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {7*11000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {8*11000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {9*11000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_15_firi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅15 fri👍\n✅✅Narxi {10*11000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_gazak_15_firi)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gazak_15_firi")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/fireee.jpg','rb'),
caption="""✅✅15 fri👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_15_firi)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/kartoshka.jpg','rb'),
caption="""✅✅Kartoshka Derevenskiy👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {1*11000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {2*11000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {3*11000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {4*11000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {5*11000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {6*11000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {7*11000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {8*11000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {9*11000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Kartoshka Derevenskiy👍\n✅✅Narxi {10*11000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_gazak_kartoshka_d)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gazak_kartoshka_d")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/kartoshka.jpg','rb'),
caption="""✅✅Kartoshka Derevenskiy👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_kartoshka_d)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == gazak menuchasi == #########################



@dp.callback_query_handler(text="guruch_katta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
caption="""✅✅Guruch Katta👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {1*11000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {2*11000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {3*11000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {4*11000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {5*11000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {6*11000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {7*11000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {8*11000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {9*11000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_guruch_kattai")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Katta👍\n✅✅Narxi {10*11000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_gazak_guruch_kattai)






####################     == gazak menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gazak_guruch_kattai")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
caption="""✅✅Guruch Katta👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_guruch_kattai)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == gazak menuchasi == #########################



@dp.callback_query_handler(text="guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
caption="""✅✅Guruch Kichchik👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_guruch_kichchik)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="birinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {1*11000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)



####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {2*11000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {3*11000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {4*11000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {5*11000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {6*11000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {7*11000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {8*11000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {9*11000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)




####################     == shaurma menuchasi == #########################



@dp.callback_query_handler(text="oninchi_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Guruch Kichchik👍\n✅✅Narxi {10*11000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_gazak_guruch_kichchik)





####################     == gazak menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gazak_guruch_kichchik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/guruch.jpg','rb'),
caption="""✅✅Guruch Kichchik👍\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_gazak_guruch_kichchik)




#################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




########################### === ichimlik bosh ==== ################################



@dp.callback_query_handler(text="ichimlik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ichimlik.jpg','rb'),
caption="""✅Marxamat Ichimliklar menusi!!!""",reply_markup=ichimlik_menu)


###########################################
#############################################################################################################
################################



@dp.callback_query_handler(text="orqaga_choy")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/ichimlik.jpg','rb'),
caption="""✅Marxamat Ichimliklar menusi!!!""",reply_markup=ichimlik_menu)

#################### == == ###################################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################








@dp.callback_query_handler(text="coffe_tea")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/choy.jpg','rb'),
caption="""✅✅Kategoriyalardan birini tanlang!!!""",reply_markup=ichimlik_menuchasi,)

####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="orqaga_choy_raqamdan")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/choy.jpg','rb'),
caption="""✅Marxamat marhamat choy va coffelar menusi!!!""",reply_markup=ichimlik_menuchasi)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == ichimlik menuchasi == #########################





@dp.callback_query_handler(text="kok_choy")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coy.jpg','rb'),
caption="""✅✅ko'k choy narxi 4000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_kok,)





####################     == 1 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="birinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {1*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 1 ta\n",reply_markup=contact_oxiri_choy_kok,)





####################     == 2 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="ikkinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {2*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 2 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 3 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="uchunchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {3*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 3 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 4 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="tortinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {4*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 4 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 5 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="beshinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {5*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 5 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 6 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oltinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {6*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 6 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 7 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="yettinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {7*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 7 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 8 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="sakiznchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {8*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 8 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 9 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="toqqizinchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {9*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 9 ta\n",reply_markup=contact_oxiri_choy_kok,)




####################     == 10 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oninchi_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅ko'k choy narxi {10*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 10 ta\n",reply_markup=contact_oxiri_choy_kok,)







####################     == ichimlik menuchasi == #########################





@dp.callback_query_handler(text="orqaga_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coy.jpg','rb'),
caption="""✅✅ko'k choy narxi 4000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_choy_kok,)















##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################









@dp.callback_query_handler(text="qora_choy")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coy.jpg','rb'),
caption="""✅✅qora choy narxi 4000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_qora,)








####################     == 1 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="birinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {1*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 1 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 2 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="ikkinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {2*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 2ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 3 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="uchunchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {3*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 3 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 4 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="tortinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {4*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 4 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 5 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="beshinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {5*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 5 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 6 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oltinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {6*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 6 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 7 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="yettinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {7*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 7 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 8 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="sakiznchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {8*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 8 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 9 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="toqqizinchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {9*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 9 ta\n",reply_markup=contact_oxiri_choy_qora,)




####################     == 10 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oninchi_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅qora choy narxi {10*4000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 10 ta\n",reply_markup=contact_oxiri_choy_qora,)






#######################################################################################################################################################



@dp.callback_query_handler(text="orqaga_choy_qorae")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coy.jpg','rb'),
caption="""✅✅qora choy narxi 4000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_qora,)






















##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == ichimlik menuchasi == #########################










@dp.callback_query_handler(text="limonli_choy_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe09.jpg','rb'),
caption="""✅✅limonli ko'k choy narxi 14000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_limon_kok,)








####################     == 1 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="birinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {1*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 1 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)





####################     == 2 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="ikkinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {2*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 2 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 3 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="uchunchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {3*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 3 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     ==4 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="tortinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {4*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 4 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 5 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="beshinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {5*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 5 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 6 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oltinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {6*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 6 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 7 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="yettinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {7*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 7 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 8 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="sakiznchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {8*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 8 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 9 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="toqqizinchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {9*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 9 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)




####################     == 10 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oninchi_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli ko'k choy narxi {10*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 10 ta\n",reply_markup=contact_oxiri_choy_limon_kok,)







####################     == ichimlik menuchasi == #########################










@dp.callback_query_handler(text="orqaga_choy_limon_kok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe09.jpg','rb'),
caption="""✅✅limonli ko'k choy narxi 14000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_limon_kok,)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################     == ichimlik menuchasi == #########################






@dp.callback_query_handler(text="limonli_choy_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe09.jpg','rb'),
caption="""✅✅limonli qora choy narxi 14000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_limon_qora,)








####################     == 1 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="birinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {1*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 1 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)





####################     == 2 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="ikkinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {2*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 2 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 3 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="uchunchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {3*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 3 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 4 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="tortinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {4*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 4 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 5 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="beshinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {5*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 5 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 6 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oltinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {6*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 6 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 7 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="yettinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {7*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 7 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 8 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="sakiznchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {8*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 8 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 9 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="toqqizinchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {9*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 9 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)






####################     == 10 =ichimlik menuchasi == #########################





@dp.callback_query_handler(text="oninchi_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅limonli qora choy narxi {10*14000} so'm\n✅✅hajmi saboy 400gr\n✅✅maxsulot soni 10 ta\n",reply_markup=contact_oxiri_choy_limon_qora,)



####################     == ichimlik menuchasi == #########################






@dp.callback_query_handler(text="orqaga_choy_limon_qora")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe09.jpg','rb'),
caption="""✅✅limonli qora choy narxi 14000 so'm\nhajmi saboy 400gr\n ✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_limon_qora,)











##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅latte narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_latte,)




####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="birinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {1*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 1 ta ",reply_markup=contact_oxiri_choy_latte,)




####################     == 2ichimlik menuchasi == #########################




@dp.callback_query_handler(text="ikkinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {2*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 2 ta ",reply_markup=contact_oxiri_choy_latte,)






####################     == 3ichimlik menuchasi == #########################




@dp.callback_query_handler(text="uchunchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {3*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 3 ta ",reply_markup=contact_oxiri_choy_latte,)






####################   4  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="tortinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {4*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 4 ta ",reply_markup=contact_oxiri_choy_latte,)






####################  5   == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="beshinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {5*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 5 ta ",reply_markup=contact_oxiri_choy_latte,)






####################   6  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oltinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {6*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 6 ta ",reply_markup=contact_oxiri_choy_latte,)






####################   7 == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="yettinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {7*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 7 ta ",reply_markup=contact_oxiri_choy_latte,)






#################### 8   == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="sakiznchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {8*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 8 ta ",reply_markup=contact_oxiri_choy_latte,)






####################   9  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="toqqizinchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {9*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 9 ta ",reply_markup=contact_oxiri_choy_latte,)






####################   10  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oninchi_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅latte narxi {10*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 10 ta ",reply_markup=contact_oxiri_choy_latte,)







####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="orqaga_choy_latte")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅latte narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_latte,)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="cappuccino")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅cappuccino narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_coppuccunio,)






####################   1  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="birinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {1*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 1 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   2 == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="ikkinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {2*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 2 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   3  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="uchunchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {3*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 3 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   4  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="tortinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {4*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 4 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   5  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="beshinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {5*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 5 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   6  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oltinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {6*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 6 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   7  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="yettinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {7*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 7 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   8  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="sakiznchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {8*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 8 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################   9  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="toqqizinchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {9*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 9 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)







####################   10  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oninchi_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅cappuccino narxi {10*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 10 ta ",reply_markup=contact_oxiri_choy_coppuccunio,)






####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="orqaga_choy_coppuccunio")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅cappuccino narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_coppuccunio,)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="americano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅americano narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_amercano,)



####################   1  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="birinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {1*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 1 ta ",reply_markup=contact_oxiri_choy_amercano,)



####################   2  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="ikkinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {2*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 2 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   3  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="uchunchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {3*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 3 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   4  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="tortinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {4*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 4 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   5  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="beshinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {5*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 5 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   6  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oltinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {6*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 6 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   7  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="yettinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {7*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 7 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   8  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="sakiznchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {8*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 8 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   9  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="toqqizinchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {9*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 9 ta ",reply_markup=contact_oxiri_choy_amercano,)




####################   10  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oninchi_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅americano narxi {10*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 10 ta ",reply_markup=contact_oxiri_choy_amercano,)






####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="orqaga_choy_amercano")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅americano narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_amercano,)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅maccoffe narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_maccoffe,)



####################   1  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="birinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {1*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 1 ta ",reply_markup=contact_oxiri_choy_maccoffe,)



####################   2  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="ikkinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {2*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 2 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   3  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="uchunchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {3*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 3 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   4  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="tortinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {4*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 4 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   5  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="beshinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {5*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 5 ta ",reply_markup=contact_oxiri_choy_maccoffe,)





####################    6  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oltinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi { 6*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 6 ta ",reply_markup=contact_oxiri_choy_maccoffe,)



####################   7  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="yettinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {7*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 7 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   8  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="sakiznchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {8*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 8 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   9  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="toqqizinchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {9*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 9 ta ",reply_markup=contact_oxiri_choy_maccoffe,)




####################   10  == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="oninchi_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅maccoffe narxi {10*12000} so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅ maxsulot sonini 10 ta ",reply_markup=contact_oxiri_choy_maccoffe,)





####################     == ichimlik menuchasi == #########################




@dp.callback_query_handler(text="orqaga_choy_maccoffe")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coffe.jpg','rb'),
caption="""✅✅maccoffe narxi 12000 so'm\nhajmi saboy 400gr\n✅✅turi coffe\n ✅✅Marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_choy_maccoffe,)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################










####################     == ichimlik menuchasi  sok == #########################



@dp.callback_query_handler(text="yaxna_ichimlik")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅✅Kategoriyalardan birini tanlang!!!',reply_markup=ichimlik_menu_sok)




####################     == ichimlik menuchasi  sok == #########################



@dp.callback_query_handler(text="orqaga__sok_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅✅Kategoriyalardan birini tanlang!!!',reply_markup=ichimlik_menu_sok)








######################################### SSSSSSSSSSSS ####################################
##############################   #####  SSS          SSS ######################################
 #####################################  SSS                                           #########################
 #####################################  SSS                                           #########################
 #####################################  SSS                                           #########################
 #####################################  SSS                                           #########################
 #####################################  SSS                                           #########################
 #####################################      SSSSSSS                                           #########################
 #####################################             SSS                                           #########################
 #####################################               SSS                                           #########################
 #####################################               SSS                                           #########################
 #####################################               SSS                                           #########################
 #####################################               SSS                                           #########################
 #####################################   SSSS        SSS                                           #########################
 #####################################      SSSSSSS                                           #########################
####################     == doda tea batafsil == #########################



@dp.callback_query_handler(text="doda_tea")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅doda teaning narxi 8000 so'm \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=raqamlar_sok_doda,)



####################     == doda tea batafsil raqamlar 1 == #########################



@dp.callback_query_handler(text="birinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {1*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)



####################     == doda tea batafsil raqamlar 2 == #########################



@dp.callback_query_handler(text="ikkinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {2*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)





####################     == doda tea batafsil raqamlar 3 == #########################



@dp.callback_query_handler(text="uchunchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {3*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)



####################     == doda tea batafsil raqamlar 4 == #########################



@dp.callback_query_handler(text="tortinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {4*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)



####################     == doda tea batafsil raqamlar 5 == #########################



@dp.callback_query_handler(text="beshinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {5*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)





####################     == doda tea batafsil raqamlar 6 == #########################



@dp.callback_query_handler(text="oltinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {6*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)





####################     == doda tea batafsil raqamlar 7 == #########################



@dp.callback_query_handler(text="yettinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {7*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)





####################     == doda tea batafsil raqamlar 8 == #########################



@dp.callback_query_handler(text="sakiznchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {8*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)




####################     == doda tea batafsil raqamlar 9 == #########################



@dp.callback_query_handler(text="toqqizinchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {9*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)



####################     == doda tea batafsil raqamlar 10 == #########################



@dp.callback_query_handler(text="oninchi_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅doda teaning narxi {10*8000} so'm\n maxsulot soni 1 ta \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_doda,)

####################     == doda tea batafsil raqamlar 10 == #########################






####################     == doda tea batafsil == #########################



@dp.callback_query_handler(text="orqaga_sok_doda")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅doda teaning narxi 8000 so'm \n masulot hajmi 1 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=raqamlar_sok_doda,)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





@dp.callback_query_handler(text="orqaga__sok_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅✅Kategoriyalardan birini tanlang!!!',reply_markup=ichimlik_menu_sok)












##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################     == ichimlik menuchasi == #########################



####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sprati.jpg','rb'),
caption="""✅✅Maxsulot narxi 6000 so'm """,reply_markup=raqamlar_sok_sprite,)
####################     == ichimlik menuchasi == #########################



####################     == doda tea batafsil raqamlar 1 == #########################



@dp.callback_query_handler(text="birinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {1*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 2 == #########################



@dp.callback_query_handler(text="ikkinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {2*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 3 == #########################



@dp.callback_query_handler(text="uchunchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {3*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 4 == #########################



@dp.callback_query_handler(text="tortinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {4*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 5 == #########################



@dp.callback_query_handler(text="beshinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {5*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar6 == #########################



@dp.callback_query_handler(text="oltinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {6*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 7 == #########################



@dp.callback_query_handler(text="yettinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {7*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 8 == #########################



@dp.callback_query_handler(text="sakiznchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {8*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 9 == #########################



@dp.callback_query_handler(text="toqqizinchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {9*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)

####################     == doda tea batafsil raqamlar 10 == #########################



@dp.callback_query_handler(text="oninchi_sok_sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅sprite teaning narxi {10*6000} so'm\n maxsulot soni 1 ta \n masulot hajmi 0,5 l \n marhamat maxsulot sonini tanlang👍👍👍 ",reply_markup=contact_oxiri_sok_sprite,)



@dp.callback_query_handler(text="orqaga_sok__sprite")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/sprati.jpg','rb'),
caption="""✅✅Maxsulot narxi 6000 so'm """,reply_markup=raqamlar_sok_sprite,)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





@dp.callback_query_handler(text="nestle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/nestli.jpg','rb'),
caption="""✅✅Maxsulot narxi 12000 so'm \n saboy stakon 400 gr \n masulot turi coffe \n marhamat maxsulot sonini tanlang👍👍👍""",reply_markup=raqamlar_sok_nesle,)



##########################  +++ 1 ++++ ##################################################





@dp.callback_query_handler(text="birinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 1 ta👍\n✅Maxsulot narxi {1*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)




##########################  +++ 2 ++++ ##################################################





@dp.callback_query_handler(text="ikkinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 2 ta👍\n✅Maxsulot narxi {2*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 3 ++++ ##################################################





@dp.callback_query_handler(text="uchunchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 3 ta👍\n✅Maxsulot narxi {3*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 4 ++++ ##################################################





@dp.callback_query_handler(text="tortinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 4 ta👍\n✅Maxsulot narxi {4*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 5 ++++ ##################################################





@dp.callback_query_handler(text="beshinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 5 ta👍\n✅Maxsulot narxi {5*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 6 ++++ ##################################################





@dp.callback_query_handler(text="oltinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 6 ta👍\n✅Maxsulot narxi {6*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 7 ++++ ##################################################





@dp.callback_query_handler(text="yettinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 7 ta👍\n✅Maxsulot narxi {7*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 8++++ ##################################################





@dp.callback_query_handler(text="sakiznchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 8 ta👍\n✅Maxsulot narxi {8*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 9 ++++ ##################################################





@dp.callback_query_handler(text="toqqizinchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 9 ta👍\n✅Maxsulot narxi {9*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)



##########################  +++ 10 ++++ ##################################################





@dp.callback_query_handler(text="oninchi_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"maxsulot sonini 10 ta👍\n✅Maxsulot narxi {10*12000} so'm \n saboy stakon 400 gr \n masulot turi coffe",reply_markup=contact_oxiri_sok_nesle,)






##########################  +++  ++++ ##################################################





@dp.callback_query_handler(text="orqaga_sok_nesle")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/nestli.jpg','rb'),
caption="""✅✅Maxsulot narxi 12000 so'm \n saboy stakon 400 gr \n masulot turi coffe \n marhamat maxsulot sonini tanlang👍👍👍""",reply_markup=raqamlar_sok_nesle,)
















##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="asu_sok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅Maxsulot narxi 7000 so'm \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=raqamlar_sok_asu,)

####################     == 1- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="birinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {1*7000 }so'm\nsoni 1 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)




####################     == 2- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {2*7000 }so'm\nsoni 2 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     ==3- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {3*7000 }so'm\nsoni 3 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 4- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {4*7000 }so'm\nsoni 4 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 5- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {5*7000 }so'm\nsoni 5 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 6- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {6*7000 }so'm\nsoni 6 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 7- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {7*7000 }so'm\nsoni 7 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 8- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {8*7000 }so'm\nsoni 8 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 9- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {9*7000 }so'm\nsoni 9 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)





####################     == 10- ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oninchi_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Maxsulot narxi {10*7000 }so'm\nsoni 10 ta \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=contact_oxiri_sok_asu,)




####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="orqaga_sok_asu")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅Maxsulot narxi 7000 so'm \n hajmi 1 l ✅✅\n masulot shirin tamli, kuchsiz gazlangan✅✅",reply_markup=raqamlar_sok_asu,)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == ichimlik menuchasi gaz  == #########################



@dp.callback_query_handler(text="gaz_sok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅✅Kategoriyalardan birini tanlang!!!',reply_markup=ichimlik_menu_gaz)




####################     == ichimlik menuchasi gaz  == #########################



@dp.callback_query_handler(text="orqaga_gaz_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅✅Kategoriyalardan birini tanlang!!!',reply_markup=ichimlik_menu_gaz)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################








####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="olmali_sok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olmali sok 11000 so'm \n ✅✅hajmi 1 l\n✅✅marxamat maxsulot sonini tanlang👍 ",reply_markup=raqamlar_gaz_olmali,)


####################   1  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="birinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {1*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 1 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   2  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {2*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 2 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   3  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {3*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 3 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   4  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {4*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 4 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   5  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {5*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 5 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   6  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {6*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 6 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   7  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {7*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 7 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   8  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {8*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 8 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   9  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {9*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 9 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################   10  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oninchi_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali sok {10*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 10 ta ",reply_markup=contact_oxiri_gaz_olmali,)




####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gaz_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olmali sok 11000 so'm \n ✅✅hajmi 1 l\n✅✅marxamat maxsulot sonini tanlang👍 ",reply_markup=raqamlar_gaz_olmali,)



####################     == ichimlik menuchasi == #########################





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="olchali_sok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olchali sok 11000 so'm \n ✅✅hajmi 1 l\n✅✅marxamat maxsulot sonini tanlang👍 ",reply_markup=raqamlar_gaz_olchali,)


####################   1  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="birinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {1*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 1 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   2  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {2*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 2 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   3 == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {3*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 3 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   4  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {4*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 4 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   5  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {5*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 5 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   6  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {6*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 6 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   7  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {7*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 7 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   8  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {8*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 8 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   9  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {9*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 9 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################   10  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oninchi_gaz_olchali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olchali sok {10*11000} so'm \n ✅✅hajmi 1 l\n✅✅maxsulot soni 10 ta ",reply_markup=contact_oxiri_gaz_olchali,)




####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="olchali_sok")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olchali sok 11000 so'm \n ✅✅hajmi 1 l\n✅✅marxamat maxsulot sonini tanlang👍 ",reply_markup=raqamlar_gaz_olchali,)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cocacola.jpg','rb'),
caption="""✅✅coca-cola 13000 so'm \n ✅✅hajmi 1.5 l\n✅✅marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_gaz_cocacola,)


####################   1  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="bircinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {1*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 1 ta ",reply_markup=contact_oxiri_gaz_cocacola,)


####################   2  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {2*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 2 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   3  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {3*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 3 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   4  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {4*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 4 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   5  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {5*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 5 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   6  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {6*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 6 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   7  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {7*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 7 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   8  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {8*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 8 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   9  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {9*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 9 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################   10  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oninchi_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅coca-cola {10*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 10 ta ",reply_markup=contact_oxiri_gaz_cocacola,)



####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gaz_cocacola")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/cocacola.jpg','rb'),
caption="""✅✅coca-cola 13000 so'm \n ✅✅hajmi 1.5 l\n✅✅marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_gaz_cocacola,)





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="pepsi")
async def knopka(call: types.CallbackQuery):
   await call.message.answer_photo(
        photo=open('images/pepsi001).jpg','rb'),
caption="""✅✅pepsi 13000 so'm \n ✅✅hajmi 1.5 l\n✅✅marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_gaz_pepsi,)


####################   1  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="birinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{1*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 1 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   2  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="ikkinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{2*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 2 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   3  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="uchunchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{3*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 3 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   4  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="tortinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{4*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 4 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   5  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="beshinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{5*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 5 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   6  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oltinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{6*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 6 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   7  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="yettinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{7*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 7 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   8  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="sakiznchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{8*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 8 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   9  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="toqqizinchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{9*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 9 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################   10  == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="oninchi_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅pepsi{10*13000} so'm \n ✅✅hajmi 1.5 l\n✅✅maxsulot soni 10 ta ",reply_markup=contact_oxiri_gaz_pepsi,)



####################     == ichimlik menuchasi == #########################



@dp.callback_query_handler(text="orqaga_gaz_pepsi")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pepsi001).jpg','rb'),
caption="""✅✅pepsi 13000 so'm \n ✅✅hajmi 1.5 l\n✅✅marxamat maxsulot sonini tanlang👍 """,reply_markup=raqamlar_gaz_pepsi,)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



########################### === desert bosh ==== ################################



@dp.callback_query_handler(text="donar")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅Marxamat danar menusi!!!""",reply_markup=donar_menu)
##################################################



########################### === desert bosh ==== ################################



@dp.callback_query_handler(text="orqaga_donar_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅Marxamat danar menusi!!!""",reply_markup=donar_menu)
##################################################


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == DANAR menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅✅Tovuqli donar👍\n✅✅Narxi 35 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="birinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {1*35000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {2*35000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {3*35000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {4*35000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {5*35000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {6*35000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {7*35000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {8*35000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {9*35000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_donar_tovuq)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="oninchi_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Tovuqli donar👍\n✅✅Narxi {10*35000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_donar_tovuq)


####################     == DANAR menuchasi == ####################################################################################################
#

@dp.callback_query_handler(text="orqaga_donar_tovuq")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅✅Tovuqli donar👍\n✅✅Narxi 35 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_donar_tovuq)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################     == DANAR menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅✅Mol go‘shtli donar👍\n✅✅Narxi 44 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="birinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {1*44000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_donar_mol)


####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {2*44000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {3*44000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_donar_mol)


####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {4*44000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {5*44000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {6*44000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {7*44000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {8*44000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {9*44000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="oninchi_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Mol go‘shtli donar👍\n✅✅Narxi {10*44000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_donar_mol)



####################     == shaurma menuchasi == #########################

@dp.callback_query_handler(text="orqaga_donar_mol")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/danar_mol.jpg','rb'),
caption="""✅✅Mol go‘shtli donar👍\n✅✅Narxi 44 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_donar_mol)



####################     == shaurma menuchasi == #########################



####################     == ichimlik menuchasi == #########################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




########################### === desert bosh ==== ################################



@dp.callback_query_handler(text="desert")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat Desert menusi!!!',reply_markup=desert_menu)


########################### === desert bosh ==== ################################



@dp.callback_query_handler(text="orqaga_desert_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer('✅Marxamat Desert menusi!!!',reply_markup=desert_menu)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/asal.jpg','rb'),
caption="""✅✅Asalim🍧\n✅✅Narxi 12 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {1*12000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {2*12000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {3*12000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {4*12000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {5*12000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {6*12000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {7*12000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {8*12000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {9*12000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_desert_assalli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Asalim🍧\n✅✅Narxi {10*12000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_desert_assalli)





####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_desert_assalli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/asal.jpg','rb'),
caption="""✅✅Asalim🍧\n✅✅Narxi 12 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_assalli)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################     == desert menuchasi == ###

####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coke.jpg','rb'),
caption="""✅✅Coke/shokoladli🍫\n✅✅Narxi 21 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_coke)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {1*21000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {2*21000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {3*21000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {4*21000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {5*21000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {6*21000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {7*21000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {8*21000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {9*21000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_desert_coke)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Coke/shokoladli🍫\n✅✅Narxi {10*21000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_desert_coke)

####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_desert_coke")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/coke.jpg','rb'),
caption="""✅✅Coke/shokoladli🍫\n✅✅Narxi 21 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_coke)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qulupnay.jpg','rb'),
caption="""✅✅Qulupnayli🍓\n✅✅Narxi 18 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {1*18000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {2*18000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {3*18000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {4*18000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {5*18000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {6*18000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {7*18000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {8*18000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {9*18000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_desert_qulupnay)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Qulupnayli🍓\n✅✅Narxi {10*18000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_desert_qulupnay)


####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_desert_qulupnay")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/qulupnay.jpg','rb'),
caption="""✅✅Qulupnayli🍓\n✅✅Narxi 18 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_desert_qulupnay)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olmali✅\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍",reply_markup=raqamlar_desert_olmali)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {1*11000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_desert_olmali)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {2*11000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {3*11000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {4*11000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {5*11000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {6*11000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {7*11000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {8*11000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {9*11000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅olmali✅\n✅✅Narxi {10*11000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_desert_olmali)


####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_desert_olmali")
async def knopka(call: types.CallbackQuery):
    await call.message.answer("✅✅olmali✅\n✅✅Narxi 11 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍",reply_markup=raqamlar_desert_olmali)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



########################### ===  pizza bosh ==== ################################



@dp.callback_query_handler(text="pizza")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅Marxamat Pizza menusi!!!""",reply_markup=pizza_menu)

####################     == desert menuchasi == #########################



########################### ===  pizza bosh ==== ################################



@dp.callback_query_handler(text="orqaga_pizza_raqamdan")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅Marxamat Pizza menusi!!!""",reply_markup=pizza_menu)


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Peperoni🍕🍕\n✅✅Narxi 57 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {1*57000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_pizza_peperoni)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {2*57000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {3*57000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {4*57000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {5*57000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {6*57000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {7*57000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {8*57000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {9*57000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Peperoni🍕🍕\n✅✅Narxi {10*57000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_pizza_peperoni)



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_pizza_peperoni")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Peperoni🍕🍕\n✅✅Narxi 57 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_peperoni)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Ananasli🍕🍕\n✅✅Narxi 63 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {1*63000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_pizza_ananasli)





####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {2*63000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {3*63000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {4*63000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {5*63000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {6*63000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {7*63000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {8*63000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {9*63000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Ananasli🍕🍕\n✅✅Narxi {10*63000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_pizza_ananasli)



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_pizza_ananasli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Ananasli🍕🍕\n✅✅Narxi 63 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_ananasli)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Margaritta🍕🍕\n✅✅Narxi 65 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_margaritta)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {1*65000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_pizza_margaritta)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {2*65000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {3*65000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {4*65000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {5*65000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {6*65000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {7*65000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {8*65000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {9*65000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Margaritta🍕🍕\n✅✅Narxi {10*65000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_pizza_margaritta)


####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_pizza_margaritta")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Margaritta🍕🍕\n✅✅Narxi 65 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_margaritta)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Pshloqli🍕🍕\n✅✅Narxi 60 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_pishloqli)



####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="birinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {1*60000}so'm\n✅✅Maxsulot soni 1 ta",reply_markup=contact_oxiri_pizza_pishloqli)




####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="ikkinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {2*60000}so'm\n✅✅Maxsulot soni 2 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="uchunchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {3*60000}so'm\n✅✅Maxsulot soni 3 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="tortinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {4*60000}so'm\n✅✅Maxsulot soni 4 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="beshinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {5*60000}so'm\n✅✅Maxsulot soni 5 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oltinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {6*60000}so'm\n✅✅Maxsulot soni 6 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="yettinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {7*60000}so'm\n✅✅Maxsulot soni 7 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="sakiznchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {8*60000}so'm\n✅✅Maxsulot soni 8 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="toqqizinchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {9*60000}so'm\n✅✅Maxsulot soni 9 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == #########################

@dp.callback_query_handler(text="oninchi_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer(f"✅✅Pshloqli🍕🍕\n✅✅Narxi {10*60000}so'm\n✅✅Maxsulot soni 10 ta",reply_markup=contact_oxiri_pizza_pishloqli)


####################     == desert menuchasi == ####################################################################################################
#


@dp.callback_query_handler(text="orqaga_pizza_pishloqli")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/pizza2.jpg','rb'),
caption="""✅✅Pshloqli🍕🍕\n✅✅Narxi 60 000 so'm\n✅✅Marhamat maxsulot sonini tanlang👍""",reply_markup=raqamlar_pizza_pishloqli)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


############################## ==== RAQAMLAR bir 1====##################################





# @dp.callback_query_handler(text="birinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 1 ta,\nNarxi:{1*5000} ming so'm  ",reply_markup=contact_oxiri)


# ############################## ==== RAQAMLAR ikki 2====##################################


# @dp.callback_query_handler(text="ikkinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 2 ta,\nNarxi:{2*5000} ming so'm ",reply_markup=contact_oxiri)



# ############################## ==== RAQAMLAR uch 3====##################################

# @dp.callback_query_handler(text="uchunchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 3 ta,\nNarxi:{3*5000} ming so'm  ",reply_markup=contact_oxiri)



# ############################## ==== RAQAMLAR tort 4====##################################

# @dp.callback_query_handler(text="tortinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 4 ta,\nNarxi:{4*5000} ming so'm  ",reply_markup=contact_oxiri)




############################## ==== RAQAMLAR besh 5====##################################



# @dp.callback_query_handler(text="beshinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 5 ta,\nNarxi:{5*5000} ming so'm ",reply_markup=contact_oxiri)


# ############################## ==== RAQAMLAR olti 6====##################################


# @dp.callback_query_handler(text="oltinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 6 ta,\nNarxi:{6*5000} ming so'm  ",reply_markup=contact_oxiri)



# ############################## ==== RAQAMLAR yetti 7====##################################


# @dp.callback_query_handler(text="yettinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 7 ta,\nNarxi:{7*5000} ming so'm ",reply_markup=contact_oxiri)



# ############################## ==== RAQAMLAR sakkiz 8 ====##################################


# @dp.callback_query_handler(text="sakiznchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 8 ta,\nNarxi:{8*5000} ming so'm \n ",reply_markup=contact_oxiri)






# ############################## ==== RAQAMLAR toqqiz 9 ====##################################


# @dp.callback_query_handler(text="toqqizinchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 9 ta,\nNarxi:{9*5000} ming so'm \n ",reply_markup=contact_oxiri)


# ############################## ==== RAQAMLAR o'n 10 ====##################################




# @dp.callback_query_handler(text="oninchi_choy")
# async def knopka(call: types.CallbackQuery):
#     await call.message.answer(f"maxsulot soni 10 ta,\nNarxi:{10*5000} ming so'm ",reply_markup=contact_oxiri)


############################## ==== RAQAMLAR yetti 7====##################################


@dp.callback_query_handler(text="eski_raqam")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""✅✅foydalanganingiz uchun rahmat""")



############################## ==== RAQAMLAR yetti 7====##################################


@dp.callback_query_handler(text="yangi_raqam")
async def knopka(call: types.CallbackQuery):
    await call.message.answer_photo(
        photo=open('images/evos.jpg','rb'),
caption="""raqamingizni kiriting!!!""",reply_markup=contact)

######################################  ===  ==== ############################################################








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
