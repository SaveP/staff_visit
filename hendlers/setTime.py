from aiogram import types, F, Router
from keyboards import otherKeyboards
import stateInfo
import time

router = Router()


@router.callback_query(F.data.startswith("time"))
async def callback_selectPersona(callback: types.CallbackQuery):
    time_bt = callback.data.split("_")[1]

    # Обработка нажатия кнопок выбора часа
    if time_bt == 'hour':
        #Если кнопку выбора часа не нажимали
        if stateInfo.get_enter_time(callback.from_user.id, 'h') == '':
            h = callback.data.split("_")[2]
            stateInfo.set_enter_time(callback.from_user.id, h=h)
            await callback.message.edit_text(
                "Выберите время, а затем нажмите Вход или Выход:",
                reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
            )

        #Если кнопку выбора часа нажимали
        elif stateInfo.get_enter_time(callback.from_user.id, 'h') != '':
            h = callback.data.split("_")[2]
            stateInfo.set_enter_time(callback.from_user.id, h='')
            await callback.message.edit_text(
                "Выберите время, а затем нажмите Вход или Выход:",
                reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
            )


    # Обработка нажатия кнопок выбора часа
    if time_bt == 'min':
        # Если кнопку выбора минуты не нажимали
            if stateInfo.get_enter_time(callback.from_user.id, 'm') == '':
                m = callback.data.split("_")[2]
                stateInfo.set_enter_time(callback.from_user.id, m=m)
                await callback.message.edit_text(
                    "Выберите время, а затем нажмите Вход или Выход:",
                    reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
                )

            # Если кнопку выбора минуты нажимали
            elif stateInfo.get_enter_time(callback.from_user.id, 'm') != '':
                m = callback.data.split("_")[2]
                stateInfo.set_enter_time(callback.from_user.id, m='')
                await callback.message.edit_text(
                    "Выберите время, а затем нажмите Вход или Выход:",
                    reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
                )


