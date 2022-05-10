% rebase('layout.tpl', title=title, year=year)


<div class="row">
    <div class="col"></div>
    <div class="col-6">
        <div class="card my-5">
            <h4 class="card-header text-center">Авторизация</h4>
            <div class="card-body">
                <form action="/auth" method="post">
                    <div class="mb-3">
                        <label for="auth_email" class="form-label">Электронная почта</label>
                        <input type="email" class="form-control" id="auth_email" placeholder="example@mail.com" name="email" required>
                    </div>
                    <div class="mb-3">
                        <label for="auth_pass" class="form-label">Пароль</label>
                        <input type="password" class="form-control" id="auth_pass" name="pass" minlength="8" maxlength="32" required>
                    </div>
                    <div class="mb-3 form-check">
                        <input type="checkbox" class="form-check-input" id="remember_me" name="remember_me">
                        <label class="form-check-label" for="remember_me">Запомнить меня</label>
                    </div>
                    <button type="submit" class="btn btn-primary">Войти</button>
                </form>
            </div>
        </div>
        <div class="card my-5">
            <h4 class="card-header text-center">Регистрация</h4>
            <div class="card-body">
                <form action="/reg" method="post">
                    <div class="mb-3">
                        <label for="reg_name" class="form-label">Ваше имя</label>
                        <input type="text" class="form-control" id="reg_name" placeholder="Иван" name="name" required>
                    </div>
                    <div class="mb-3">
                        <label for="reg_email" class="form-label">Электронная почта</label>
                        <input type="email" class="form-control" id="reg_email" aria-describedby="reg_email_help" placeholder="example@mail.com" name="email" required>
                        <div id="reg_email_help" class="form-text">Мы не будет ни с кем делится вашей почтой.</div>
                    </div>
                    <div class="mb-3">
                        <label for="reg_pass" class="form-label">Придумайте пароль</label>
                        <input type="password" class="form-control" id="reg_pass" name="pass" minlength="8" maxlength="32" required>
                        <div id="reg_email_help" class="form-text">Пароль должен содержать минимум 8 символов.<br>Разрешённые символы: A-Z, a-z, 0-9, _, -</div>
                    </div>
                    <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
                </form>
            </div>
        </div>
    </div>
    <div class="col"></div>
</div>
