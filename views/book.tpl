% rebase('layout.tpl', title=title, year=year)
<h2 class="my-4">{{ ', '.join(a.name for a in book.authors_rel) }}</h2>
<h3 class="my-3">{{ book.name }}</h3>
<div class="row"><!--Разделение странички на 2 секции, через класс row-->
    <div class="col-ld-3 col-md-3 col-mb-3"><!--Размер первого блока-->
        <div class="cl2">
            <img src="/book/image/{{ book.id }}.jpg" width = 300px>
        </div>
    </div>
    <div class="col-ld-9 col-md-9 col-mb-9"><!--Размер второго блока(с информацией о книгах)-->
        <div class="cl1">
            <p>Год издания: {{ book.year }}</p>
            <p>Артикул: {{ book.isbn }}</p>
            <p>Рейтинг: {{ book.rating }}</p>
            <h3>Описание</h3>
            <p>{{ book.description }}</p><!--Кнопки для взаимодействий-->
            <button type="button" class="btn btn-primary">Купить за {{ book.price }}</button>
        </div>
    </div>
    <div class="col col-mb-0"></div>
    <div class="col-9 col-mb-12">
        <div class="card my-5">
            <h4 class="card-header text-center">Оставьте свой отзыв</h4>
            <div class="card-body">
                <form action="/review" method="post">
                    <input type="hidden" name="book" value="{{ book.id }}">
                    <div class="mb-3">
                        <label for="review-mark" class="form-label">Как вы оцениваете данную книгу</label>
                        <input type="number" class="form-control" id="review-mark" min="0" max="10" name="review-mark" style="min-width: 100%;" required>
                    </div>
                    <div class="mb-3">
                        <label class="review-content">Ваш отзыв:</label>
                        <textarea class="form-control" id="review-content" rows="5" name="review-content" style="min-width: 100%;"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Отправить</button>
                </form>
            </div>
        </div>
    </div>
</div>