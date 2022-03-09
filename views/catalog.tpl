% rebase('layout.tpl', title=title, year=year)

<h1 class="my-5">
    Каталог\\
    %if filter == 'popular':
         - По популярности\\
    %end
    %if filter == 'rating':
         - По рейтингу\\
    %end
</h1>

<div class="row">
    %for book in books.values():
        <div class="col-lg-3 col-md-4 col-sm-6 mb-4">
            <div class="card">
                <img src="/static/images/{{ book.code }}.jpg" alt="{{ book.code }}.jpg" class="card-top-img">
                <div class="card-body">
                    <h5 class="card-title">{{ book.name }}</h5>
                </div>
                <ul class="list-group list-group-flush">
                    <li class="list-group-item">
                        %for name in book.authors:
                            <p class="m-0">{{ name }}</p>
                        %end
                    </li>
                    <li class="list-group-item">Цена: {{ book.price }}p.</li>
                </ul>
                <div class="card-body">
                    <a href="/book/{{ book.code }}" class="btn btn-primary" role="button">Купить</a>
                </div>
            </div>
        </div>
    %end
</div>
