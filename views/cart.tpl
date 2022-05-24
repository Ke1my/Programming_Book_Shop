% rebase('layout.tpl', title=title, year=year)

<!-- Заголовок каталога. Вставка применённого стиля -->
<h2 class="my-4">Корзина</h2>
<!-- Сетка -->
<div class="row">
    %if len(user.cart_rel) == 0:
    <h3 class="display-5">Корзина пуста.</h3>
    %end
    %for book in user.cart_rel:
    <!-- Ячейка -->
    <div class="col-lg-3 col-md-4 col-sm-6 mb-4">
        <div class="card">
            <!-- Фото обложки -->
            <img src="/book/image/{{ book.id }}.jpg" alt="{{ book.id }}.jpg" class="card-top-img">
            <div style="position: relative;">
                <div class="rating-container"><span class="rating">{{ book.rating }}</span></div>
            </div>
            <div class="card-body">
                <h5 class="card-title">{{ book.name }}</h5>
            </div>
            <div class="card-body">
            </div>
        </div>
    </div>
    %end
    
    %if len(user.cart_rel) != 0:
    <form action="/confirm" method="post">
        <!-- Поля с адресом и номером телефона -->
        <label class="form-label">Телефон</label>
        <input type="text" class="form-control" name="phone_number" style="min-width: 100%;" required>
        <br/>
        <label class="form-label">Адресс</label>
        <input type="text" class="form-control" name="adress" style="min-width: 100%;" required>
        <button type="submit" class="btn btn-primary">Оформить заказ</button>
    </form>
    %end
</div>