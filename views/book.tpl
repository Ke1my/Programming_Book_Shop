% rebase('layout.tpl', title=title, year=year)

<style> .cl1 {display: inline-block; width = 100px; margin-top: 10px; margin-left: 10px}
button{margin-top: 5px}
.cl2 {display: inline-block;width = 100px; border: 5px solid black} 
</style>
<h2>{{author}}</h2>
<h3>{{name}}</h3>
<div class="cl2">
<img src="static\img\{{code}}.jpg" width = 300px>
</div>
<div class="cl1">
<button type="<button" class="btn btn-info">Купить за {{price}}</button>
</br>
<button type="button" class="btn btn-info">Удалить из корзины</button>
</br>
<p>Год издания: {{bookyear}}</p>
<p>Артикул: {{isbn}}</p>
<p>Рейтинг: {{rating}}</p>
<h3>Описание</h3>
<p>{{description}}</p>
</div>
