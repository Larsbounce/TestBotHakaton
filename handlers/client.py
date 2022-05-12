from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_main,kb_self_1,kb_self_2,kb_self_3,kb_self_4
from handlers import other as oth
from aiogram.dispatcher import FSMContext

count = 0

async def start(message: types.Message):
    await message.reply('Привет это тестовый бот',reply_markup=kb_main)


async def math_start(message: types.Message):
        await oth.FSMath.percent.set()
        await message.reply('1. Сотая часть числа?')

async def math_percent(message: types.Message,state: FSMContext):
        async with state.proxy() as data:
            data['percent'] = message.text.lower()
        await oth.FSMath.next()
        await message.reply('2. Что легче: 1 кг ваты или 1 кг железа?')

async def weight(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('3. Может ли при умножении получиться ноль?')



async def multiply_zero( message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['multiply_zero'] = message.text.lower()
        await oth.FSMath.next()
        await message.reply('4. Чему равна четверть часа?')

async def quater_hour(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['quater_hour'] = message.text.lower()
        await oth.FSMath.next()
        await message.reply('5. Специфическая единица измерения обьёма нефти?')

async def math_barrel(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['barrel'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('6. Первая координата точки ? ')
async def math_absc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['absc'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('7. Наука изучающая свойства фигур на плоскости ? ')

async def math_planemetriya(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['planemetriya'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('8. Прибор для измерения углов ?')

async def math_transportir(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['transportir'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('''9. Учёный, наиболее известным достижением 
                        которого стало «решето» для отсеивания простых чисел?''')
async def math_eratosthenes(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['eratosthenes'] = message.text.lower()
    await oth.FSMath.next()
    await message.reply('10. Утверждение, требующее доказательства?')
async def math_teorema(message: types.Message, state: FSMContext):
    count = 0
    res = 0
    async with state.proxy() as data:
        data['teorema'] = message.text.lower()
        for i in data.keys():
            if data[i] == 'процент' or data[i] == 'одинаково' or data[i] == 'да' or data[i] == '15 мин.' or data[i] == 'Баррель' or data[i] == 'абсцисса' or data[i] == 'планиметрия' or data[i] == 'транспортир' or data[i] == 'эратосфен' or data[i] == 'теорема':
                count += 1
    res = count * 10
    await state.finish()
    await message.reply(f'Тест пройден на {res}%')




async def self(message: types.Message):
    await oth.FSSelf.holidays.set()
    await message.reply(' Вы совершенно измотаны, неделя была долгой и не самой удачной. Как проведете выходные?',reply_markup=kb_self_1)
async def self_holidays(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        print(message.text)
        data['holidays'] = str(message.text)[0]

    await oth.FSSelf.next()
    await message.reply('Какое из двух описаний больше подходит вам?',reply_markup=kb_self_2)

async def one_or_two(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['one_or_two'] = message.text[0]
    await oth.FSSelf.next()
    await message.reply('Компания - конкурент вашего работодателя пытается вас переманить. Вы сомневаетесь: там гораздо больше платят,но здесь прекрасный коллектив, да и начальник отдела намекнул, что рекомендует вас руководству перед уходом на пенсию. Как будете принимать решение?',reply_markup=kb_self_3)

async def company(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company'] = message.text[0]
    await oth.FSSelf.next()
    await message.reply('До свадьбы ваших близких друзей 2 недели. Как дела с подготовкой?',reply_markup=kb_self_4)

async def mary(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['mary'] = message.text[0]
        count = ''
        ls = []
        for i in data.keys():
            ls.append(data[i])
        count = ls[0] + ls[1] + ls[2] + ls[3]

        if count == 'ESTJ':
            await message.reply('Ты УПРАВЛЕНЕЦ',reply_markup=kb_main)
        if count == 'ENTJ':
            await message.reply('Ты КОМАНДИР',reply_markup=kb_main)
        if count == 'ESFJ':
            await message.reply('Ты УЧИТЕЛЬ',reply_markup=kb_main)
        if count == 'ESTP':
            await message.reply('Ты МАРШАЛ',reply_markup=kb_main)
        if count == 'ENFJ':
            await message.reply('Ты НАСТАВНИК',reply_markup=kb_main)
        if count == 'ENTP':
            await message.reply('Ты ИЗОБРЕТАТЕЛЬ',reply_markup=kb_main)
        if count == 'ESFP':
            await message.reply('Ты ПОЛИТИК',reply_markup=kb_main)
        if count == 'ENFP':
            await message.reply('Ты ЧЕМПИОН',reply_markup=kb_main)
        if count == 'INFP':
            await message.reply('Ты ЦЕЛИТЕЛЬ',reply_markup=kb_main)
        if count == 'ISFP':
            await message.reply('Ты КОМПОЗИТОР',reply_markup=kb_main)
        if count == 'INTP':
            await message.reply('Ты АРХИТЕКТОР',reply_markup=kb_main)
        if count == 'INFJ':
            await message.reply('Ты СОВЕТНИК',reply_markup=kb_main)
        if count == 'INTJ':
            await message.reply('Ты ВДОХНОВИТЕЛЬ',reply_markup=kb_main)
        if count == 'ISFJ':
            await message.reply('Ты ЗАЩИТНИК',reply_markup=kb_main)
        if count == 'ISTP':
            await message.reply('Ты УМЕЛЕЦ',reply_markup=kb_main)
        if count == 'ISTJ':
            await message.reply('Ты ИНСПЕКТОР',reply_markup=kb_main)
    await state.finish()










def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start','👍'])
    dp.register_message_handler(math_start, Text(equals='Математика', ignore_case=True),state=None)
    dp.register_message_handler(math_percent, state=oth.FSMath.percent)
    dp.register_message_handler(weight,state=oth.FSMath.mass)
    dp.register_message_handler(multiply_zero,state = oth.FSMath.multiplicate)
    dp.register_message_handler(quater_hour,state=oth.FSMath.hour)
    dp.register_message_handler(math_barrel,state=oth.FSMath.barrel)
    dp.register_message_handler(math_absc,state=oth.FSMath.abscis)
    dp.register_message_handler(math_planemetriya,state=oth.FSMath.planimetry)
    dp.register_message_handler(math_transportir,state=oth.FSMath.protractor)
    dp.register_message_handler(math_eratosthenes,state=oth.FSMath.eratosthenes)
    dp.register_message_handler(math_teorema,state=oth.FSMath.theorem)
    dp.register_message_handler(self,Text(equals='Тест на личность',ignore_case=True),state=None)
    dp.register_message_handler(self_holidays,state=oth.FSSelf.holidays)
    dp.register_message_handler(company,state=oth.FSSelf.company)
    dp.register_message_handler(one_or_two,state=oth.FSSelf.one_or_two)
    dp.register_message_handler(mary,state=oth.FSSelf.marry)