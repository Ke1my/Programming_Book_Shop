% rebase('layout.tpl', title=title, year=year)


<div class="column">
    <div class="col-2">
        <h2 class="my-4">Авторизация</h2>
        <p>Почта:</p>
        <input type="email" name="autmail">
        <p>Пароль:</p>
        <input type="password" name="autpass">
        <button type="button" class="btn btn-primary mt-4">Авторизироваться</button>
    </div>
    <div class="col-2">
        <form action="/reg" method="reg">
           <h2 class="my-4">Регистрация</h2>
           <p>Имя:</p>
           <input type="text" name="regname" required minlength="4" maxlength="20" size="20">
           <p>Почта:</p>
           <input type="email" name="regmail">
           <p>Пароль:</p>
           <input type="password" name="regpass">
           <p>Проверка пароля:</p>
           <input type="password" name="regpasscheck">
           <button type="button" onclick="" class="btn btn-primary mt-4">Зарегистрироваться</button>
        </form>
    </div>
</div>
