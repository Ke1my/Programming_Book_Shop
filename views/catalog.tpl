% rebase('layout.tpl', title=title, year=year)

<!-- Заголовок каталога. Вставка применённого стиля -->
<h1 class="my-5">
    Каталог\\
    %if filter == 'new':
         - Новинки\\
    %end
    %if filter == 'popular':
         - По популярности\\
    %end
    %if filter == 'rating':
         - По рейтингу\\
    %end
</h1>

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
                <form action="/add" method="post" class="catalog-hidden-form">
                    <input type="hidden" name="book" value="{{ book.id }}">
                    <button type="submit" class="btn btn-primary">Купить</button>
                </form>
                    <!-- Ссылка на страницу с книгой -->
                    <a href="/book/{{ book.id }}" class="btn btn-primary" role="button">Открыть</a>

                </div>
            </div>
        </div>
    %end
</div>
