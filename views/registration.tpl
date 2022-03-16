% rebase('layout.tpl', title=title, year=year)


<div class="row">
       <div class="col"></div>
       <div class="col-2">
             <!-- Заголовок -->
              <h2 class="my-4">Регистрация</h2>
              <!-- Поля для ввода -->
              <p>Ник:</p>
              <input type="text" id="name" name="name" required minlength="4" maxlength="8" size="10">
              <p>Пароль:</p>
              <input type="text" id="name" name="name" required minlength="4" maxlength="8" size="10">
              <p>Повторите ваш пароль:</p>
              <input type="text" id="name" name="name" required minlength="4" maxlength="8" size="10">
              <button type="button" class="btn btn-primary mt-4">Создать</button>
       </div>
       <div class="col"></div>
</div>
