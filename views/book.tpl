% rebase('layout.tpl', title=title, year=year)

<style>
    .cl1 {
        display: inline-block;
        width: 100px;
        margin-top: 10px;
        margin-left: 10px
    }
    button {
        margin-top: 5px
    }
    .cl2 {
        display: inline-block;
        width: 100px;
        border: 5px solid black
    }
</style>

<h2>{{ ', '.join(book.authors) }}</h2>
<h3>{{ book.name }}</h3>
<div class="cl2">
    <img src="/static/images/{{ book.code }}.jpg" width = 300px>
</div>
<div class="cl1">
    <button type="<button" class="btn btn-info">Купить за {{ book.price }}</button>
    </br>
    <button type="button" class="btn btn-info">Удалить из корзины</button>
    </br>
    <p>Год издания: {{ book.year }}</p>
    <p>Артикул: {{ book.isbn }}</p>
    <p>Рейтинг: {{ book.rating }}</p>
    <h3>Описание</h3>
    <p>{{ book.description }}</p>
</div>
