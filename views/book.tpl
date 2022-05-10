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
</div>

