% import urllib
% import string
<div class="container">
<div class="row">
    <div class="col-md-12">
        <ul class="nav nav-tabs">
            % if single is not True:
                % for name in names:
                    % currentName = name.translate(string.maketrans("",""),string.punctuation)
                    <li><a href="#{{currentName}}" data-toggle="tab">{{urllib.unquote_plus(name)}} <span class="badge">{{len(list[names.index(name)].items())}}</span></a></li>
                % end
            % else:
                    % currentName = names[0].translate(string.maketrans("",""),string.punctuation)
                    <li class="active"><a href="#{{currentName}}" data-toggle="tab">{{urllib.unquote_plus(names[0])}} <span class="badge">{{len(list[0].items())}}</span></a></li>
            % end
        </ul>
        <br>
        <div class="tab-content">
        % for answerLine in list:
            % if single is True:
                % currentName = names[list.index(answerLine)].translate(string.maketrans("",""),string.punctuation)
                <div class="tab-pane active" id="{{currentName}}">
            % else:
                % currentName = names[list.index(answerLine)].translate(string.maketrans("",""),string.punctuation)
                <div class="tab-pane" id="{{currentName}}">
            % end
            <h3>Showing results for {{urllib.unquote_plus(names[list.index(answerLine)])}}</h3>
            <table class="table table-striped sortable table-bordered">
            <thead>
            <tr>
                <th>Word</th>
                % if single is not True:
                    <th>TF-IDF</th>
                % end
                <th>Rank</th>
                % url = 'quinterest.org/php/search.php?info=' + names[list.index(answerLine)] + '&categ=' + category + '&difficulty=' + difficulty + '&stype=Answer&tournamentyear=All'
                <th><a href="{{ ''.join(['http://', url]) }}">Tossups</a></th>
                <th>Earliness</th>
            </tr>
            </thead>
            <tbody>
            % for word in answerLine.items():
                <tr>
                    <td>{{word[0]}}</td>
                    % if single is not True:
                        <td>{{word[1]['tf-idf']}}</td>
                    % end
                    <td>{{word[1]['rank']}}</td>
                    <td>{{word[1]['tossups']}}</td>
                    <td>{{word[1]['earliness']}}</td>
                </tr>
            % end
            </tbody>
            </table>
            </div>
        % end
        </div>
        </div>
    </div>
</div>
