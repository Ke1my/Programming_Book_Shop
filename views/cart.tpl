% rebase('layout.tpl', title=title, year=year)

<!-- Заголовок каталога. Вставка применённого стиля -->
<h2 class="my-4">Корзина</h2>
<!-- Сетка -->
<div class="row">
    %for book in books:
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
                <!-- Авторы книги -->
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        %for author in book.authors_rel:
                            <p class="m-0">{{ author.name }}</p>
                        %end
                    </li>
                    <li class="list-group-item">Цена: {{ book.price }}p.</li>
                </ul>
                <div class="card-body">
                </div>
            </div>
        </div>
    %end
</div>
<form action="/confirm" method="post">
<button type="submit" class="btn btn-primary">Оформить заказ</button>
</form>