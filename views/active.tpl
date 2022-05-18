% rebase('layout.tpl', title=title, year=year)

<h2 class="my-4">{{ title }}</h2>

<div class="row">
    <div class="col"></div>
    <div class="col-9">
        % if len(users) == 0:
        <div class="text-center">
            <h3 class="display-3">У нас нет активных пользователей(((</h3>
        </div>
        % end
        %for (user, count) in users:
            <div class="card mb-4">
                <div class="card-body">
                    <p class="m-0">Пользователь <strong>{{ user.name }}</strong> написал {{ count }} отзыв(ов)</p>
                </div>
            </div>
        %end
    </div>
    <div class="col"></div>
</div>
