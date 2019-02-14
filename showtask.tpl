%rebase("base.tpl")


<h1 style="font-size: 40px;">タスク一覧だよー＼(^o^)／</h1>

<div class="row" style="margin:0 auto;">
  
<table class="table table-bordered" border="1">
      
    <thead>
        <tr>
        % for header_tpl in headers_tpl:
            <th>{{header_tpl}}</th>
        % end
        </tr>
    </thead>
        
    <tbody>
        % for task_list in task_list_tpl:
            <tr>
                <td>{{task_list["id"]}}</td>
                <td>{{task_list["task"]}}</td>
                <td>{{task_list["time"]}}</td>
                <td><a href="/delete/{{task_list['id']}}">削除</a></td>
            </tr>
        % end

    </tbody>
    </table>
</div>

<a href="http://127.0.0.1:8080/index"> トップページへ</a>
<button><a href="http://127.0.0.1:8080/add"> タスク追加へ</a></button> 
<a href="http://127.0.0.1:8080/dbtest"> 戻る</a>