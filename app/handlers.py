from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}') # from_user - хранит всю информацию (first_name, last_name, full_name, является ли premium, может ли вступать в группы, номер телефона при  и т.д.)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help')

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIDA2Y8CC6Te9D4rLmITz12H-K0yhUWAAKb1TEb4kzgSRGwEFB0HjnFAQADAgADeQADNQQ' #Также можно указывать и url
                               ,caption='Это сегодняшний прикол с тачкой, мотом и снегом!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото {message.photo[-1].file_id}') # [-1] - лучшее качество
