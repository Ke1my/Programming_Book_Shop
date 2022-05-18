% rebase('layout.tpl', title=title, year=year)

<!-- Создание классов со свойствами и задание свойств-->
<!-- Заголовки -->
<h2>Профиль</h2>
<h3>{{user.name}}</h3>
<h3>{{user.email}}</h3>
<!-- Кнопки -->
<div class="cl1">
    <a href="/cart" class="btn btn-primary">Корзина</a>
</div>
