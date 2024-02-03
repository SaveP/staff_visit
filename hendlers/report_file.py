from aiogram import types, Router
from aiogram.filters.command import Command

from data_base import db_to_exel
from aiogram.types import FSInputFile

router = Router()

@router.message(Command("getreport"))
async def cmd_start(message: types.Message):
    db_to_exel.create_report_to_xlsx()
    file_path = 'report.xlsx'
    file = FSInputFile(file_path, filename=file_path)
    await message.answer_document(file)


@router.message(Command("getfullreport"))
async def cmd_start(message: types.Message):
    db_to_exel.create_full_report_to_xlsx()
    file_path = 'fullreport.xlsx'
    file = FSInputFile(file_path, filename=file_path)
    await message.answer_document(file)
