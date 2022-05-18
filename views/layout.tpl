<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CoolBookShop - {{ title }}</title>
    <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/css/site.css" />
</head>

<body>
    <div class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-lg">
            <a class="navbar-brand" href="/">CoolBookShop</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggler" aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarToggler">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item"><a href="/home" class="nav-link">Главная</a></li>
                    <li class="nav-item dropdown">
                        <a href="#" class="nav-link dropdown-toggle" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">Каталог</a>
                        <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">
                            <li><a href="/catalog/recent" class="dropdown-item">Все книги</a></li>
                            <li><a href="/catalog/new" class="dropdown-item">Новинки</a></li>
                            <li><a href="/catalog/popular" class="dropdown-item">По популярности</a></li>
                            <li><a href="/catalog/rating" class="dropdown-item">По рейтингу</a></li>
                        </ul>
                    </li>
                    <li class="nav-item"><a href="/profile" class="nav-link">Профиль</a></li>
                    <li class="nav-item"><a href="/active" class="nav-link">Активные пользователи</a></li>
                    <li class="nav-item"><a href="/about" class="nav-link">О нас</a></li>
                </ul>
                <span class="navbar-text">
                    %if request.get_cookie('userhash') == None:
                        <a href="/auth" class="nav-link">Вход</a>
                    %end
                    %if request.get_cookie('userhash') != None:
                        <a href="/logout" class="nav-link">Выйти</a>
                    %end
                </span>
            </div>
        </div>
    </div>
    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - CoolBookShop</p>
        </footer>
    </div>

    <script src="/static/scripts/bootstrap.bundle.js"></script>

</body>
</html>
