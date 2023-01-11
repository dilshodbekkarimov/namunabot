from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
#######################TELFON RAQAM#############################


contact = ReplyKeyboardMarkup(
	keyboard = [
					[
						KeyboardButton(text = 'raqamni yuborish', request_contact=True),
					],
				],
	resize_keyboard=True
)

########################################LOKATSIYA#################################


location = ReplyKeyboardMarkup(
	keyboard = [
					[
						KeyboardButton(text = 'joylashuvingizni yuboring!!!', request_location=True),
					],
				],
	resize_keyboard=True
)


###################### TILNI TANLANG ######################################

til = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="🇺🇿 O'zbekcha",callback_data='uz'),
					],
					[
						InlineKeyboardButton(text="🇷🇺 Russian",callback_data='ru'),
					],
					[
						InlineKeyboardButton(text="🇺🇸 English",callback_data='eng'),
					],
				],
)

########################  PASTKI MENU ################################

menu = ReplyKeyboardMarkup(
	keyboard = [
					[
						KeyboardButton(text="🍽 maxsulotlar"),
					],
					[
						KeyboardButton(text="☎️ Aloqa"),
					],
					[
						KeyboardButton(text="⚙️ Sozlamalar"),
					],
				],
	resize_keyboard=True
)



#####################MAXSULOTLAR MENUSI##########################


bosh_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Lavash🌯🌯",callback_data='lavash'),
						InlineKeyboardButton(text="Hod Dog🌭🌭",callback_data='hoddog'),
					],
					[
						InlineKeyboardButton(text="Sendvich clib🥪🥪",callback_data='sendvich'),
						InlineKeyboardButton(text="Burger🍔🍔",callback_data='burger'),
					],
					[
						InlineKeyboardButton(text="Shaurma🌮🌮",callback_data='shaurma'),
						InlineKeyboardButton(text="Donar🍱🍱",callback_data='donar'),
					],
					[
						InlineKeyboardButton(text="Gazaklar🍟🍟",callback_data='gazak'),
						InlineKeyboardButton(text="Ichimliklar🧋🍹",callback_data='ichimlik'),
					],
					[
						InlineKeyboardButton(text="Desertlar🍰🍰",callback_data='desert'),
						InlineKeyboardButton(text="Pizza🍕🍕",callback_data='pizza'),
					],
				],
)



##################################### lavash menu##########################



lavash_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Mol go‘shtlik🥩",callback_data='lavash_mol'),
						InlineKeyboardButton(text="Tovuq go‘shtlik 🍗",callback_data='lavash_tovuq'),
					],
					[
						InlineKeyboardButton(text="Qalampirli Mol go‘shtlik🥩🌶",callback_data='lavash_mol_q'),
						InlineKeyboardButton(text="Qalampirli Tovuq go‘shtlik 🍗",callback_data='lavash_tovuq_q'),
					],					
					[
						InlineKeyboardButton(text="Fitter🥬🥬",callback_data='fitter'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga01'),
					],
				],
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################














###########################################################################################################
############################## lavash menulari 01#########################
###################################################################################




lavash_menu_mol = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Classik👍",callback_data='lavash_mol_classik'),
						InlineKeyboardButton(text="Mini👍",callback_data='lavash_mol_mini'),
						],
						[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash'),
					],
				],
)


##########################  +++  ++++ ##################################################







raqamlar_lavash_mol_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_mol_classik'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_mol_classik'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_mol_classik'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_mol_classik'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_mol_classik'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_mol_classik'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_mol_classik'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_mol_classik'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_mol_classik'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_mol_classik'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan_mol_cm'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_mol_mini = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_mol_mini'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_mol_mini'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_mol_mini'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_mol_mini'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_mol_mini'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_mol_mini'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_mol_mini'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_mol_mini'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_mol_mini'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_mol_mini'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan_mol_cm'),
					],
				],
)





###########################################################################################################
############################## lavash menulari tovuq  classil  va mini #########################
###################################################################################




lavash_menu_tovuq = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Classik👍",callback_data='lavash_tovuq_classik'),
						InlineKeyboardButton(text="Mini👍",callback_data='lavash_tovuq_mini'),
						],
						[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash'),
					],
				],
)


##########################  +++  ++++ ##################################################







raqamlar_lavash_tovuq_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_tovuq_classik'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_tovuq_classik'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_tovuq_classik'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_tovuq_classik'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan_toviq_dm'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_tovuq_mini = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_tovuq_mini'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_tovuq_mini'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_tovuq_mini'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_tovuq_mini'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan_toviq_dm'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_mol_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_mol_q'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_mol_q'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_mol_q'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_mol_q'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_mol_q'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_mol_q'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_mol_q'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_mol_q'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_mol_q'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_mol_q'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_tovuq_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_tovuq_q'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_tovuq_q'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_tovuq_q'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_tovuq_q'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_mol_p = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_mol_p'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_mol_p'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_mol_p'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_mol_p'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_mol_p'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_mol_p'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_mol_p'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_mol_p'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_mol_p'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_mol_p'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_tovuq_p = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_tovuq_p'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_tovuq_p'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_tovuq_p'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_tovuq_p'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_lavash_fittr = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_lavash_fittr'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_lavash_fittr'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_lavash_fittr'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_lavash_fittr'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_lavash_fittr'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_lavash_fittr'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_lavash_fittr'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_lavash_fittr'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_lavash_fittr'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_lavash_fittr'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_raqamdan'),
					],
				],
)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################













############################### ==  HODDOG BOSH = ######################################################
##################################################################################


hoddog_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Hod Dog Baget Dabl👍",callback_data='baget_hoddog'),
						InlineKeyboardButton(text="Classik Hod dog👍",callback_data='classik_hoddog'),
					],
					[
 						InlineKeyboardButton(text="Korolevsiky👍",callback_data='kar_hoddog'),
						InlineKeyboardButton(text="Tovuqli Hod Dog👍",callback_data='tovuqli_hoddog'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)





#############################################################################################
##########################===== hoddog raqamlar =========############################




raqamlar_hoddog_baget = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_hoddog_baget'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_hoddog_baget'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_hoddog_baget'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_hoddog_baget'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_hoddog_baget'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_hoddog_baget'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_hoddog_baget'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_hoddog_baget'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_hoddog_baget'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_hoddog_baget'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_raqamdan'),
					],
				],
)








#############################################################################################
##########################===== hoddog raqamlar =========############################




raqamlar_hoddog_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_hoddog_classik'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_hoddog_classik'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_hoddog_classik'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_hoddog_classik'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_hoddog_classik'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_hoddog_classik'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_hoddog_classik'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_hoddog_classik'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_hoddog_classik'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_hoddog_classik'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_raqamdan'),
					],
				],
)








#############################################################################################
##########################===== hoddog raqamlar =========############################




raqamlar_hoddog_kar = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_hoddog_kar'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_hoddog_kar'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_hoddog_kar'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_hoddog_kar'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_hoddog_kar'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_hoddog_kar'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_hoddog_kar'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_hoddog_kar'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_hoddog_kar'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_hoddog_kar'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_raqamdan'),
					],
				],
)








#############################################################################################
##########################===== hoddog raqamlar =========############################




raqamlar_hoddog_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_hoddog_tovuqli'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_hoddog_tovuqli'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_hoddog_tovuqli'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_hoddog_tovuqli'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_raqamdan'),
					],
				],
)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






################################# == SHAURMA BOSH =  ####################################################
##################################################################################


shaurma_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Mol go‘shtli Shaurma👍",callback_data='shaurma_mol'),
						InlineKeyboardButton(text="Tovuqli Shaurma👍",callback_data='shaurma_tovuq'),
					],
					[
 						InlineKeyboardButton(text="Qalampirli Mol go‘shtli Shaurma👍",callback_data='shaurma_mol_q'),
						InlineKeyboardButton(text="Qalanpirli Tovuqli Shaurma👍",callback_data='shaurma_tovuq_q'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)






#############################################################################################
##########################===== shaurma raqamlar =========############################




raqamlar_shaurma_mol = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_shaurma_mol'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_shaurma_mol'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_shaurma_mol'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_shaurma_mol'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_shaurma_mol'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_shaurma_mol'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_shaurma_mol'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_shaurma_mol'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_shaurma_mol'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_shaurma_mol'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_raqamdan'),
					],
				],
)








#############################################################################################
##########################===== shaurma raqamlar =========############################




raqamlar_shaurma_tovuq = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_shaurma_tovuq'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_shaurma_tovuq'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_shaurma_tovuq'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_shaurma_tovuq'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_shaurma_tovuq'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_shaurma_tovuq'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_shaurma_tovuq'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_shaurma_tovuq'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_shaurma_tovuq'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_shaurma_tovuq'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_raqamdan'),
					],
				],
)







#############################################################################################
##########################===== shaurma raqamlar =========############################




raqamlar_shaurma_mol_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_shaurma_mol_q'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_shaurma_mol_q'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_shaurma_mol_q'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_shaurma_mol_q'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_shaurma_mol_q'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_shaurma_mol_q'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_shaurma_mol_q'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_shaurma_mol_q'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_shaurma_mol_q'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_shaurma_mol_q'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_raqamdan'),
					],
				],
)








#############################################################################################
##########################===== shaurma raqamlar =========############################




raqamlar_shaurma_tovuq_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_shaurma_tovuq_q'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_shaurma_tovuq_q'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_shaurma_tovuq_q'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_shaurma_tovuq_q'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_raqamdan'),
					],
				],
)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################









############################# == SENDVICH BOSH =  ########################################################
##################################################################################


sendvich_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Tovuqli Sendvich👍",callback_data='tovuqli_sendvich'),
						InlineKeyboardButton(text="Classik Sendvich Club👍",callback_data='classik_sendvich'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)



raqamlar_sendvich_c = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sendvich_c'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sendvich_c'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sendvich_c'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sendvich_c'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sendvich_c'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sendvich_c'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sendvich_c'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sendvich_c'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sendvich_c'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sendvich_c'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sendvich_raqamdan'),
					],
				],
)




############################# == SENDVICH BOSH =  ########################################################
##################################################################################



raqamlar_sendvich_ct = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sendvich_ct'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sendvich_ct'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sendvich_ct'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sendvich_ct'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sendvich_ct'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sendvich_ct'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sendvich_ct'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sendvich_ct'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sendvich_ct'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sendvich_ct'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sendvich_raqamdan'),
					],
				],
)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




############################### ==  BURGER BOSH = ######################################################
##################################################################################


burger_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Gamburger👍",callback_data='gamburger'),
						InlineKeyboardButton(text="Chizburger👍",callback_data='chizburger'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)


raqamlar_gamburger = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_gamburger'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_gamburger'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_gamburger'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_gamburger'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_gamburger'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_gamburger'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_gamburger'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_gamburger'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_gamburger'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_gamburger'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_burger_raqamdan'),
					],
				],
)



############################### ==  BURGER BOSH = ######################################################
##################################################################################



raqamlar_chizburger = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_chizburger'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_chizburger'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_chizburger'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_chizburger'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_chizburger'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_chizburger'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_chizburger'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_chizburger'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_chizburger'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_chizburger'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_burger_raqamdan'),
					],
				],
)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




################################# == DONAR BOSH == ####################################################
##################################################################################


donar_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Tovuqli donar👍",callback_data='donar_tovuq'),
						InlineKeyboardButton(text="Mol go‘shtli donar👍",callback_data='donar_mol'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)





raqamlar_donar_mol = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_donar_mol'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_donar_mol'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_donar_mol'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_donar_mol'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_donar_mol'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_donar_mol'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_donar_mol'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_donar_mol'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_donar_mol'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_donar_mol'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_donar_raqamdan'),
					],
				],
)






################################# == DONAR BOSH == ####################################################
##################################################################################



raqamlar_donar_tovuq = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_donar_tovuq'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_donar_tovuq'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_donar_tovuq'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_donar_tovuq'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_donar_tovuq'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_donar_tovuq'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_donar_tovuq'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_donar_tovuq'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_donar_tovuq'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_donar_tovuq'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_donar_raqamdan'),
					],
				],
)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




############################### == GAZAK BOSH = ######################################################
##################################################################################


gazak_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="15 fri👍",callback_data='15_firi'),
						InlineKeyboardButton(text="Kartoshka Derevenskiy👍",callback_data='kartoshka_d'),
					],
					[
 						InlineKeyboardButton(text="Guruch Katta👍",callback_data='guruch_katta'),
						InlineKeyboardButton(text="Guruch Kichchik👍",callback_data='guruch_kichchik'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)






############################### == GAZAK BOSH = ######################################################
##################################################################################



raqamlar_gazak_15_firi = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_15_firi'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_15_firi'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_15_firi'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_15_firi'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_15_firi'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_15_firi'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_15_firi'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_15_firi'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_15_firi'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_15_firi'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_raqamdan'),
					],
				],
)






############################### == GAZAK BOSH = ######################################################
##################################################################################



raqamlar_gazak_kartoshka_d = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_kartoshka_d'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_kartoshka_d'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_kartoshka_d'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_kartoshka_d'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_kartoshka_d'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_kartoshka_d'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_kartoshka_d'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_kartoshka_d'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_kartoshka_d'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_kartoshka_d'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_raqamdan'),
					],
				],
)





############################### == GAZAK BOSH = ######################################################
##################################################################################



raqamlar_gazak_guruch_kattai = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_guruch_kattai'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_guruch_kattai'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_guruch_kattai'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_guruch_kattai'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_guruch_kattai'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_guruch_kattai'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_guruch_kattai'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_guruch_kattai'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_guruch_kattai'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_guruch_kattai'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_raqamdan'),
					],
				],
)





############################### == GAZAK BOSH = ######################################################
##################################################################################



raqamlar_gazak_guruch_kichchik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_guruch_kichchik'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_guruch_kichchik'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_guruch_kichchik'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_guruch_kichchik'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_guruch_kichchik'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_guruch_kichchik'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_guruch_kichchik'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_guruch_kichchik'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_guruch_kichchik'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_guruch_kichchik'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_raqamdan'),
					],
				],
)






##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


############################### = ICHIMLIK  BOSH = ######################################################
##################################################################################


ichimlik_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Tea vs Cofe☕️",callback_data='coffe_tea'),
						InlineKeyboardButton(text="Yaxna ichimliklar🧃",callback_data='yaxna_ichimlik'),
					],
					[
 						InlineKeyboardButton(text="Gazli va Tabiiy Soklar🥤🍸",callback_data='gaz_sok'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)


############################### = ICHIMLIK menuchasi = ######################################################
##################################################################################


ichimlik_menuchasi = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Ko'k choy🫖🫖",callback_data='kok_choy'),
						InlineKeyboardButton(text="Qora choy🫖🫖",callback_data='qora_choy'),
					],
					[
 					
 						InlineKeyboardButton(text="Limonli ko‘k choy🫖🫖",callback_data='limonli_choy_kok'),
 						InlineKeyboardButton(text="Limonli qora choy🫖🫖",callback_data='limonli_choy_qora'),

					],
										[
 					
 						InlineKeyboardButton(text="Latte☕️",callback_data='latte'),
 						InlineKeyboardButton(text="Cappuccino☕️",callback_data='cappuccino'),

					],					[
 					
 						InlineKeyboardButton(text="Americano☕️",callback_data='americano'),
 						InlineKeyboardButton(text="Maccoffe☕️",callback_data='maccoffe'),

					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy'),
					],
				],
)
############################### = ICHIMLIK  menuchasi 2 = ######################################################
##################################################################################


ichimlik_menu_sok = InlineKeyboardMarkup(


	inline_keyboard = [
					[
						InlineKeyboardButton(text="Doda tea🧃 🧃",callback_data='doda_tea'),
						InlineKeyboardButton(text="Sprite🧃🧃",callback_data='sprite'),
					],
					[
					 	InlineKeyboardButton(text="Nestle🧃🧃",callback_data='nestle'),
 						InlineKeyboardButton(text="Asu🧃",callback_data='asu_sok'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy'),
					],
				],
)

############################### = ICHIMLIK  menuchasi 3 = ######################################################
##################################################################################


ichimlik_menu_gaz = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Olmali sok🧃",callback_data='olmali_sok'),
						InlineKeyboardButton(text="Olchali sok🧃",callback_data='olchali_sok'),
					],
					[
					 	InlineKeyboardButton(text="Coca-Cola 🍷",callback_data='cocacola'),
 						InlineKeyboardButton(text="Pepsi🍷",callback_data='pepsi'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy'),
					],
				],
)
#











##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################

##########################  +++  ++++ ##################################################






raqamlar_choy_kok = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_kok'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_kok'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_kok'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_kok'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_kok'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_kok'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_kok'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_kok'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_kok'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_kok'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)




##########################  +++  ++++ ##################################################






raqamlar_choy_qora = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_qora'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_qora'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_qora'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_qora'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_qora'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_qora'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_qora'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_qora'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_qora'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_qora'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_limon_kok = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_limon_kok'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_limon_kok'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_limon_kok'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_limon_kok'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_limon_kok'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_limon_kok'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_limon_kok'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_limon_kok'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_limon_kok'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_limon_kok'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_limon_qora = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_limon_qora'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_limon_qora'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_limon_qora'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_limon_qora'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_limon_qora'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_limon_qora'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_limon_qora'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_limon_qora'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_limon_qora'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_limon_qora'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_latte = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_latte'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_latte'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_latte'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_latte'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_latte'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_latte'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_latte'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_latte'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_latte'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_latte'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_coppuccunio = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_coppuccunio'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_coppuccunio'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_coppuccunio'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_coppuccunio'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_coppuccunio'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_coppuccunio'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_coppuccunio'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_coppuccunio'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_coppuccunio'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_coppuccunio'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_amercano = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_amercano'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_amercano'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_amercano'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_amercano'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_amercano'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_amercano'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_amercano'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_amercano'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_amercano'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_amercano'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################






raqamlar_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy_maccoffe'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy_maccoffe'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy_maccoffe'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy_maccoffe'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy_maccoffe'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy_maccoffe'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy_maccoffe'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy_maccoffe'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy_maccoffe'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy_maccoffe'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################

##########################  +++  ++++ ##################################################



##########################  +++  ++++ ##################################################







raqamlar_sok_doda = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sok_doda'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sok_doda'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sok_doda'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sok_doda'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sok_doda'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sok_doda'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sok_doda'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sok_doda'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sok_doda'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sok_doda'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga__sok_raqamdan'),
					],
				],
)


##########################  +++  ++++ ##################################################







raqamlar_sok_sprite = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sok_sprite'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sok_sprite'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sok_sprite'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sok_sprite'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sok_sprite'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sok_sprite'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sok_sprite'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sok_sprite'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sok_sprite'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sok_sprite'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga__sok_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################







raqamlar_sok_nesle = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sok_nesle'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sok_nesle'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sok_nesle'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sok_nesle'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sok_nesle'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sok_nesle'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sok_nesle'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sok_nesle'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sok_nesle'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sok_nesle'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga__sok_raqamdan'),
					],
				],
)









##########################  +++  ++++ ##################################################







raqamlar_sok_asu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_sok_asu'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_sok_asu'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_sok_asu'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_sok_asu'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_sok_asu'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_sok_asu'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_sok_asu'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_sok_asu'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_sok_asu'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_sok_asu'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga__sok_raqamdan'),
					],
				],
)




##########################  +++  ++++ ##################################################




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################











raqamlar_gaz_olmali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_gaz_olmali'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_gaz_olmali'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_gaz_olmali'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_gaz_olmali'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_gaz_olmali'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_gaz_olmali'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_gaz_olmali'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_gaz_olmali'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_gaz_olmali'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_gaz_olmali'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_raqamdan'),
					],
				],
)





raqamlar_gaz_olchali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_gaz_olchali'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_gaz_olchali'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_gaz_olchali'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_gaz_olchali'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_gaz_olchali'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_gaz_olchali'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_gaz_olchali'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_gaz_olchali'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_gaz_olchali'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_gaz_olchali'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_raqamdan'),
					],
				],
)

raqamlar_gaz_cocacola = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='bircinchi_gaz_cocacola'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_gaz_cocacola'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_gaz_cocacola'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_gaz_cocacola'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_gaz_cocacola'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_gaz_cocacola'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_gaz_cocacola'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_gaz_cocacola'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_gaz_cocacola'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_gaz_cocacola'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_raqamdan'),
					],
				],
)

raqamlar_gaz_pepsi = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_gaz_pepsi'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_gaz_pepsi'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_gaz_pepsi'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_gaz_pepsi'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_gaz_pepsi'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_gaz_pepsi'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_gaz_pepsi'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_gaz_pepsi'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_gaz_pepsi'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_gaz_pepsi'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_raqamdan'),
					],
				],
)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






##########################  +++  ++++ ##################################################







raqamlar_choy = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)








##########################  +++  ++++ ##################################################







raqamlar_choy = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)









##########################  +++  ++++ ##################################################







raqamlar_choy = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)





##########################  +++  ++++ ##################################################







raqamlar_choy = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)








##########################  +++  ++++ ##################################################







raqamlar_choy = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_choy'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_choy'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_choy'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_choy'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_choy'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_choy'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_choy'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_choy'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_choy'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_choy'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_raqamdan'),
					],
				],
)

##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################




############################### ==  desert BOSH = ######################################################
##################################################################################


desert_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Asalim🍧 ",callback_data='assalli'),
						InlineKeyboardButton(text="Coke/shokoladli🍫",callback_data='coke'),
					],
					[
 						InlineKeyboardButton(text="Qulupnayli🍓",callback_data='qulupnay'),
						InlineKeyboardButton(text="olmali✅ ",callback_data='olmali'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)



############################### == DESERT BOSH = ######################################################
##################################################################################



raqamlar_desert_assalli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_assalli'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_assalli'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_assalli'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_assalli'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_assalli'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_assalli'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_assalli'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_assalli'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_assalli'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_assalli'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_raqamdan'),
					],
				],
)



############################### == DESERT BOSH = ######################################################
##################################################################################



raqamlar_desert_coke = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_coke'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_coke'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_coke'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_coke'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_coke'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_coke'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_coke'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_coke'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_coke'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_coke'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_raqamdan'),
					],
				],
)



############################### == DESERT BOSH = ######################################################
##################################################################################



raqamlar_desert_qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_qulupnay'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_qulupnay'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_qulupnay'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_qulupnay'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_qulupnay'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_qulupnay'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_qulupnay'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_qulupnay'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_qulupnay'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_qulupnay'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_raqamdan'),
					],
				],
)



############################### == DESERT BOSH = ######################################################
##################################################################################



raqamlar_desert_olmali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_olmali'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_olmali'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_olmali'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_olmali'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_olmali'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_olmali'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_olmali'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_olmali'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_olmali'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_olmali'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_raqamdan'),
					],
				],
)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







############################# == PIZZA BOSH = ########################################################
##################################################################################


pizza_menu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="Peperoni🍕🍕",callback_data='peperoni'),
						InlineKeyboardButton(text="Ananasli🍕🍕",callback_data='ananasli'),
					],
					[
 						InlineKeyboardButton(text="Margaritta🍕🍕",callback_data='margaritta'),
						InlineKeyboardButton(text="Pshloqli🍕🍕",callback_data='pishloqli'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_bosh'),
					],
				],
)




############################### == PIZZA BOSH = ######################################################
##################################################################################



raqamlar_pizza_peperoni = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_peperoni'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_peperoni'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_peperoni'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_peperoni'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_peperoni'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_peperoni'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_peperoni'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_peperoni'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_peperoni'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_peperoni'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_raqamdan'),
					],
				],
)


############################### == PIZZA BOSH = ######################################################
##################################################################################



raqamlar_pizza_ananasli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_ananasli'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_ananasli'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_ananasli'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_ananasli'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_ananasli'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_ananasli'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_ananasli'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_ananasli'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_ananasli'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_ananasli'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_raqamdan'),
					],
				],
)


############################### == PIZZA BOSH = ######################################################
##################################################################################



raqamlar_pizza_margaritta = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_margaritta'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_margaritta'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_margaritta'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_margaritta'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_margaritta'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_margaritta'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_margaritta'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_margaritta'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_margaritta'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_margaritta'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_raqamdan'),
					],
				],
)


############################### == PIZZA BOSH = ######################################################
##################################################################################



raqamlar_pizza_pishloqli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text="1⃣",callback_data='birinchi_pishloqli'),
						InlineKeyboardButton(text="2⃣",callback_data='ikkinchi_pishloqli'),
    					InlineKeyboardButton(text="3⃣",callback_data='uchunchi_pishloqli'),
						InlineKeyboardButton(text="4⃣",callback_data='tortinchi_pishloqli'),
						InlineKeyboardButton(text="5⃣",callback_data='beshinchi_pishloqli'),
					],
					[
						InlineKeyboardButton(text="6⃣",callback_data='oltinchi_pishloqli'),
						InlineKeyboardButton(text="7⃣",callback_data='yettinchi_pishloqli'),
						InlineKeyboardButton(text="8⃣",callback_data='sakiznchi_pishloqli'),
						InlineKeyboardButton(text="9⃣",callback_data='toqqizinchi_pishloqli'),
						InlineKeyboardButton(text="🔟",callback_data='oninchi_pishloqli'),
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_raqamdan'),
					],
				],
)


##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################





####################################== == == == == ==#####################################################

contact_oxiri = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_00'),
					],
				],
	
)

####################################== == == == == ==#####################################################

contact_oxiri_sok_doda = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sok_doda'),
					],
				],
	
)


####################################== ==contact_oxiri_sok_sprite == contact_oxiri_sok_sprite== == ==#####################################################

contact_oxiri_sok_sprite = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sok__sprite'),
					],
				],
	
)





####################################== ==nesle  nesle  nesle  nesle == == == ==#####################################################

contact_oxiri_sok_nesle = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sok_nesle'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_sok_asu = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sok_asu'),
					],
				],
	
)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################


####################################== == == == == ==#####################################################

contact_oxiri_choy_kok = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_kok'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_qora = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_qorae'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_limon_kok = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_limon_kok'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_limon_qora= InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_limon_qora'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_latte = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_latte'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_coppuccunio = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_coppuccunio'),
					],
				],
	
)




####################################== == == == == ==#####################################################

contact_oxiri_choy_amercano = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_amercano'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_maccoffe'),
					],
				],
	
)







##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################################== == == == == ==#####################################################

contact_oxiri_gaz_olmali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_olmali'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_gaz_olchali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_olchali'),
					],
				],
	
)


####################################== == == == == ==#####################################################

contact_oxiri_gaz_cocacola = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_cocacola'),
					],
				],
	
)


####################################== == == == == ==#####################################################

contact_oxiri_gaz_pepsi = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gaz_pepsi'),
					],
				],
	
)



##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################










####################################== == == == == ==#####################################################

contact_oxiri_lavash_mol_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_mol_classik'),
					],
				],
	
)


	

####################################== == == == == ==#####################################################

contact_oxiri_lavash_mol_mini = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_mol_mini'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_tovuq_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_tovuq_classik'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_tovuq_mini = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_tovuq_mini'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_mol_p = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_mol_p'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_tovuq_p = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_tovuq_p'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_mol_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_mol_q'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_lavash_tovuq_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_tovuq_q'),
					],
				],
	
)





####################################== == == == == ==#####################################################

contact_oxiri_lavash_fittr = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_lavash_fittr'),
					],
				],
	
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################










####################################== == == == == ==#####################################################

contact_oxiri_hoddog_baget = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_baget'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_hoddog_classik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_classik'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_hoddog_kar = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_kar'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_hoddog_tovuqli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_hoddog_tovuqli'),
					],
				],
	
)




##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################






####################################== == == == == ==#####################################################

contact_oxiri_shaurma_mol = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_mol'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_shaurma_tovuq = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_tovuq'),
					],
				],
	
)








####################################== == == == == ==#####################################################

contact_oxiri_shaurma_mol_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_mol_q'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_shaurma_tovuq_q = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_shaurma_tovuq_q'),
					],
				],
	
)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################








####################################== == == == == ==#####################################################

contact_oxiri_sendvich_c = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sendvich_c'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_sendvich_ct = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_sendvich_ct'),
					],
				],
	
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################



####################################== == == == == ==#####################################################

contact_oxiri_gamburger = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gamburger'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_chizburger = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_chizburger'),
					],
				],
	
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







####################################== == == == == ==#####################################################

contact_oxiri_donar_tovuq = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_donar_tovuq'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_donar_mol = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_donar_mol'),
					],
				],
	
)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







####################################== == == == == ==#####################################################

contact_oxiri_pizza_pishloqli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_pishloqli '),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_pizza_margaritta = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_margaritta'),
					],
				],
	
)








####################################== == == == == ==#####################################################

contact_oxiri_pizza_ananasli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_ananasli'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_pizza_peperoni = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_pizza_peperoni'),
					],
				],
	
)








##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







####################################== == == == == ==#####################################################

contact_oxiri_desert_qulupnay = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_qulupnay'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_desert_olmali = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_olmali'),
					],
				],
	
)








####################################== == == == == ==#####################################################

contact_oxiri_desert_coke = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_coke'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_desert_assalli = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_desert_assalli'),
					],
				],
	
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







####################################== == == == == ==#####################################################

contact_oxiri_gazak_guruch_kichchik = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_guruch_kichchik'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_gazak_guruch_kattai = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_guruch_kattai'),
					],
				],
	
)








####################################== == == == == ==#####################################################

contact_oxiri_gazak_kartoshka_d = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_kartoshka_d'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_gazak_15_firi = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_gazak_15_firi'),
					],
				],
	
)









##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################
##########################  +++  ++++ ##################################################







####################################== == == == == ==#####################################################

contact_oxiri_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_maccoffe'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_maccoffe'),
					],
				],
	
)








####################################== == == == == ==#####################################################

contact_oxiri_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_maccoffe'),
					],
				],
	
)



####################################== == == == == ==#####################################################

contact_oxiri_choy_maccoffe = InlineKeyboardMarkup(
	inline_keyboard = [
					[
						InlineKeyboardButton(text='✅✅eski manzil va raqamdan foyudalanish',callback_data="eski_raqam"),
						InlineKeyboardButton(text='✅✅yamgi manzil va raqam kiritish',callback_data="yangi_raqam"),						
					],
					[
						InlineKeyboardButton(text="🔄orqaga",callback_data='orqaga_choy_maccoffe'),
					],
				],
	
)




