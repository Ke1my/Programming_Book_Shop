% rebase('layout.tpl', title=title, year=year)

<style>
    <!--Класс для блока информации-->
    .cl1 { 
     
        display: inline-block;
        width: 1000px;
        margin-top: 20px;
        margin-left: 30px;
    }
    button {
        margin-top: 5px;
    }
    <!--Класс для картинки-->
    .cl2 {
        margin-top: 20px;
        display: inline-block;
        width: 300px;
    }
</style>

<h2>{{ ', '.join(book.authors) }}</h2>
<h3>{{ book.name }}</h3>
<div class="row"><!--Разделение странички на 2 секции, через класс row-->
<div class="col-ld-3 col-md-3 col-mb-3"><!--Размер первого блока-->
    <div class="cl2">
    <img src="/static/images/{{ book.code }}.jpg" width = 300px>
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
    <button type="button" class="btn btn-primary">Добавить в список желаний</button>
  </div>
  </div>
</div>
