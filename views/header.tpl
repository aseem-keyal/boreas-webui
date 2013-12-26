<!DOCTYPE html>
<html lang="en">
<head>
    <title>Boreas</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="/static/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="/static/theme.css">
    <link rel="stylesheet" type="text/css" href="/static/examples.css">
    <link rel="shortcut icon" href="/static/favicon.ico">
    <script src="/static/sorttable.js"></script>
    <script src="/static/jquery.js"></script>
    <script src="/static/typeahead.min.js"></script>
    <script src="/static/bootstrap.min.js"></script>
    <script>
        $( document ).ready(function() {
            $('#typeahead').typeahead({
                name: 'answerLines',
                prefetch: '/static/answerLines_HS.json',
                limit: 10
            });
            add_fields = function(){
                var numbers = $('input').length
                console.log(numbers)
                var formgroup = document.createElement("div");
                formgroup.className = "form-group";
                document.getElementById('wrapper').appendChild(formgroup);

                var label = document.createElement("label");
                label.className = "col-sm-2 control-label";
                formgroup.appendChild(label);

                var div = document.createElement("div");
                div.className = "col-sm-10";
                formgroup.appendChild(div);

                var input = document.createElement("input");
                input.className = "form-control";
                input.id = "typeahead" + (numbers - 3).toString();
                input.name = "answerLine";
                input.placeholder = "Enter additional answer line";
                input.type = "text";
                div.appendChild(input);
                $('#typeahead' + (numbers - 3).toString()).typeahead({
                    name: 'answerLines',
                    prefetch: '/static/answerLines_HS.json',
                    limit: 10
                });
            };
            var myTH = document.getElementsByTagName("th")[1];
            sorttable.innerSortFunction.apply(myTH, []);

        });
    </script>
</head>
<body>
