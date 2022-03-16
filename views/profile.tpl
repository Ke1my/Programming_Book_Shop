% rebase('layout.tpl', title=title, year=year)

<!-- Создание классов со свойствами и задание свойств-->
<style>
    .cl1 {
        display: inline-block;
        margin-top: 10px;
        margin-left: 10px
    }
    button {
        margin-top: 5px
    }
    .cl2 {
        display: inline-block;
        border: 5px solid black
    } 
</style>

<!-- Заголовки -->
<h2>Профиль</h2>
<h3>Андрей Лебедев</h3>

<!-- Аватарка -->
<div class="cl2">
    <img src="static\images\ava.jpg" width = 300px>
</div>
<!-- Кнопки -->
<div class="cl1">
    <button type="button" class="btn btn-primary">Список желаний</button>
    </br>
    <button type="button" class="btn btn-primary">История покупок</button>
    </br>
    <button type="button" class="btn btn-primary">Изменить информацию профиля</button>
</div>
