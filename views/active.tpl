% rebase('layout.tpl', title=title, year=year)

<h2 class="my-4">{{ title }}</h2>

<div class="row">
    <div class="col"></div>
    <div class="col-9">
        %for (user, count) in users:
            <p class="m-0">{{ user.name }} - {{ user.email }}: {{ count }}</p>
        %end
    </div>
    <div class="col"></div>
</div>
