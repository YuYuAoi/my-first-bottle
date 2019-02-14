%rebase("base.tpl")


<table class="table table-bordered" border="1">
    <thead>
        <tr>
        % for header_tpl in headers_tpl:
            <th>{{header_tpl}}</th>
        % end
        </tr>
    </thead>
        
    <tbody>
        % for user_list in user_list_tpl:
            <tr>
                <td>{{user_list["name"]}}</td>
                <td>{{user_list["age"]}}</td>
                <td>{{user_list["address"]}}</td>
            </tr>
        % end
    </tbody>
</table>

<a href="http://127.0.0.1:8080/index"> トップページへ</a>
<a href="http://127.0.0.1:8080/dbtest"> 戻る</a>