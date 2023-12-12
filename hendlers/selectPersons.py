from aiogram import types, F, Router

from keyboards import selectPersons, otherKeyboards, mainMenu
from hendlers.mainMenu import callMainMenu
import stateInfo

router = Router()


@router.callback_query(F.data.startswith("selectPersona"))
async def callback_selectPersona(callback: types.CallbackQuery):
    personalId = callback.data.split("_")[1]

    # Обработка нажатия кнопки 'Next'
    if personalId == 'Next':
        if stateInfo.selectedPersonal_is_empty(callback.from_user.id):
          await callback.answer('Выберите людей')
          return
        else:
            await callback.message.edit_text(
                "Выберите действие:",
                reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
            )
            return

    # Обработка нажатия кнопки 'Cancel'
    if personalId == 'Cancel':
        await callMainMenu(callback)
        return


    stateInfo.updateSelectPersons(callback.from_user.id, int(personalId))
    await callback.message.edit_text(
        "Выберите людей:",
        reply_markup=selectPersons.selectPersonKb(callback.from_user.id)
    )

    await callback.answer()
