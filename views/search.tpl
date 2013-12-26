<div class="navbar navbar-fixed-top navbar-default">
<div class="container">
                <div class="navbar-header">
                  <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-inverse-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                  </button>
                  <a class="navbar-brand" href="http://akeyal.dyndns.org:82/search">Boreas</a>
                </div>
                <div class="navbar-collapse collapse navbar-inverse-collapse">
                  <ul class="nav navbar-nav">
                    <li><a href="http://github.com/aseem-keyal/boreas-webui">Github</a></li>
                  </ul>
                  <ul class="nav navbar-nav navbar-right">
                    <li><a href="mailto:aseem.keyal@gmail.com">Contact Me</a></li>
                  </ul>
                </div><!-- /.nav-collapse -->
              </div>
</div>
<div class="container">
        <div class="row">
        <div class="col-md-12">
        <div class="well well-lg">
        <h1>Search</h1>
        <form action="/search" method="get" class="form form-horizontal" role="form">
            <div id="wrapper">
            <div class="form-group">
                <label for="answerLine" class="col-sm-2 control-label">Answer Line:</label>
                <div class="col-sm-10">
                    <input type="text" class="form-control" id="typeahead" name="answerLine" placeholder="Enter an answer line">
                </div>
            </div>
            </div>
            <div class="form-group">
                <label for="optionCategory" class="col-sm-2 control-label">Category:</label>
                <div class="col-sm-10">
                    <select class="form-control" name="category" id="optionCategory">
                        <option value="All">All</option>
                        <option value="Literature">Literature</option>
                        <option value="History">History</option>
                        <option value="Science">Science</option>
                        <option value="Fine Arts">Fine Arts</option>
                        <option value="Trash">Trash</option>
                        <option value="Mythology">Mythology</option>
                        <option value="Philosophy">Philosophy</option>
                        <option value="Social Socience">Social Science</option>
                        <option value="Religion">Religion</option>
                        <option value="Geography">Geography</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label for="optionDifficulty" class="col-sm-2 control-label">Difficulty:</label>
                <div class="col-sm-10">
                    <select class="form-control" name="difficulty" id="optionDifficulty">
                        <option value="All">All</option>
                        <option value="MS">Middle School</option>
                        <option value="HS">High School</option>
                        <option value="College">College</option>
                        <option value="Open">Open</option>
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label for="case" class="col-sm-2 control-label">Filter by case:</label>
                <div class="col-sm-10">
                    <input type="radio" name="case" id="case" value="lower"> Lower
                    <input type="radio" name="case" id="case" value="upper"> Upper
                </div>
            </div>
            <div class="form-group">
                <div class="col-sm-offset-2 col-sm-10">
                    <button value="Search" type="submit" class="btn btn-primary">Search</button>
                    <a class="btn btn-default" onclick="add_fields();">Add answer line</a>
                </div>
           </div>
</form>
</div>
</div>
</div>
</div>
